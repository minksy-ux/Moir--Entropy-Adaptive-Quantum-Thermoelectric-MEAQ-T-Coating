# MEAQ-T Coating: Computational Roadmap

**Status**: Multi-scale modeling pipeline development plan  
**Last Updated**: 2026-07-15  
**Target Platforms**: VASP, Quantum ESPRESSO, LAMMPS, OOMMF, Abaqus/COMSOL

---

## Modeling Hierarchy & Coupling

```
Quantum Scale (DFT)
├─ VASP / Quantum ESPRESSO
├─ Compute: Electronic band structure, phonon dispersion
├─ Output: K-points, DOS, transport coefficients (raw)
│
├─ [Boltzmann Transport Bridge]
│
Mesoscale (Boltzmann Transport)
├─ BoltzTraP2 / custom Boltzmann solver
├─ Compute: Seebeck, conductivity, thermal conductivity
├─ Input: DFT band structure, scattering relaxation time (τ)
├─ Output: Transport coefficients vs. T, doping level
│
├─ [Tight-Binding Extraction]
│
Atomic Scale (Tight-Binding / ML Models)
├─ Wannier90 interpolation
├─ Compute: Moire band structure, flat bands
├─ For large systems: Machine-learned potential (e.g., GAP, SNAP)
├─ Output: Effective masses, density of states enhancement
│
├─ [Micromagnetic Bridge]
│
Magnetic Scale (Micromagnetics)
├─ OOMMF / Magpar
├─ Compute: Domain structure, spin dynamics, pulse response
├─ Input: Magnetic parameters (K_u, M_s, exchange)
├─ Output: Magnetization evolution, switching dynamics
│
├─ [Phase-Field / Continuum Bridge]
│
Damage Scale (Phase-Field & FEM)
├─ COMSOL / Abaqus + custom code
├─ Compute: Crack initiation, healing kinetics, thermal stress
├─ Input: Elastic moduli, fracture toughness, thermal properties
├─ Output: Stress distribution, damage evolution, healing rate
│
Device Scale (Integrated Simulation)
└─ Coupled solver (COMSOL multiphysics or custom Python)
   ├─ Thermoelectric: ∇T → electrical current (via Seebeck)
   ├─ Magnetic: Pulse → magnetization → thermal output
   ├─ Mechanical: Thermal cycling → stress → damage
   └─ Healing: Damage + heat → closure kinetics
```

---

## Level 1: Quantum Scale (DFT) – Band Structure & Phonons

### 1.1 HEA Interlayer Properties

**System**: Equiatomic oxide (Hf, Zr, Ta, Nb, Ti)O or high-entropy variant

**VASP Input Template**:
```
# INCAR: High-accuracy DFT calculation
SYSTEM = MEAQT-HEA
ENCUT = 500 eV          (high precision)
ISMEAR = 0; SIGMA = 0.05 (electronic smearing)
NSW = 100; IBRION = 2   (structure relaxation)
POTCAR: PAW potentials (Hf, Zr, Ta, Nb, Ti, O) - all-electron or PAW
KPOINTS: Monkhorst-Pack 6×6×6 (convergence)
```

**Output**: 
- Band structure (along high-symmetry paths)
- Phonon dispersion (via DFPT, IBRION=8)
- Elastic tensor (stress-strain calculation)
- Dielectric function ε(ω) for optical properties

**Key Properties**:
- Band gap E_g (indirect transitions relevant for thermal transport)
- Electron-phonon coupling λ (deformation potential)
- Debye temperature Θ_D
- Sound velocities (longitudinal/transverse)

**Computational Cost**: 
- Single-point: ~100 CPU-hours per composition
- Full phonon spectrum: ~1,000 CPU-hours
- Scaling: ~5–10 compositions in parallel (100 atoms ~80 k-points)

### 1.2 2D Moire Heterostructure (MoTe₂/WSe₂)

**System**: Small supercell with twist angle θ (1.1° typical)

**Approach**:
- Build 1.1° twisted bilayer (supercell ~100–200 atoms)
- Relax atomic positions (keep lattice mostly rigid)
- Calculate electronic structure with HSE hybrid functional (band gap accuracy)

**VASP specifics**:
- ALGO = Exact (for hybrid functional, more expensive)
- ENCUT = 400 eV (adequate for transition metals + chalcogens)
- KPOINTS: Smaller k-mesh for large supercell (4×4×1 typical)

**Output**:
- Flat band structure near Fermi level (indicating moire trapping)
- Local density of states (LDOS) enhancement at band edges
- Wannier interpolation for tight-binding model

**Computational Cost**: 
- Supercell relax: 50–200 CPU-hours
- Band structure + HSE: 500–1,000 CPU-hours per composition
- Multiple twist angles: 2,000–5,000 CPU-hours per pair (MoTe₂/WSe₂)

### 1.3 Vitrimer / Polymer Interface

**System**: Organic-inorganic interface (smaller supercell, semi-empirical methods acceptable)

**Approach**:
- DFT study of H-bonding and charge transfer at interface
- Estimate adhesion energy: E_adhesion = E_total - E_polymer - E_inorganic
- Use B3LYP functional (good for organic/inorganic hybrids)

**Computational Cost**: 
- Moderate (50–200 atoms per interface)
- 100–300 CPU-hours per configuration

---

## Level 2: Boltzmann Transport – Thermoelectric Coefficients

### 2.1 Pipeline: DFT → BoltzTraP2 → Transport Coefficients

**Tool**: BoltzTraP2 (open-source Python package)

**Input**: VASP electronic band structure (EIGENVAL, KPOINTS files)

**Process**:
1. Read VASP output and interpolate band structure on fine k-mesh (~20×20×20 k-points)
2. Integrate transport integrals:
   - Seebeck: $S = \frac{1}{eT} \int \frac{(E-E_F)^2}{4\cosh^2(E-E_F/2k_BT)} \sigma(E) dE$
   - Conductivity: $\sigma = e \int \tau(E) v^2(E) \frac{\partial f}{\partial E} \pi D(E) dE$
   - Thermal conductivity: Wiedemann-Franz + lattice contribution from phonons

3. Sweep over:
   - Temperature: 200–1200 K (device operating range)
   - Carrier concentration: ±10²⁰ cm⁻³ (via Fermi level shift)
   - Scattering relaxation time τ: tune to match experiment (typically 1–10 fs)

4. Extract optimal ZT curve and doping level

**Key Input Uncertainty**: Relaxation time τ (not from DFT alone)
- Estimate from electron-phonon coupling (λ from HSE DFT)
- Calibrate against experimental data (literature Seebeck for similar materials)
- Sensitivity: τ affects σ linearly; ZT ∝ τ

**Output**:
- Seebeck S(T, n) heatmap
- Conductivity σ(T, n) heatmap
- Power factor PF(T, n) = σS²
- Optimal doping n_opt and corresponding ZT_peak

**Typical Results** (HEA oxide):
- S = 50–150 µV/K (depending on τ)
- σ = 100–500 S/cm
- κ_e (electronic) ≈ 0.1–1 W/m-K
- κ_lattice ≈ 1–3 W/m-K
- ZT ≈ 0.1–0.3 (depending on composition)

**Computational Cost**: 
- DFT band structure: 500–2,000 CPU-hours (one-time per material)
- BoltzTraP2 transport: 10–50 CPU-hours per parametric sweep
- Full optimization (5 compositions × 10 doping levels × 5 temperatures): ~500 CPU-hours

---

## Level 3: Moire Band Structure & Tight-Binding Extraction

### 3.1 Wannier Interpolation (DFT → Tight-Binding)

**Tool**: Wannier90 (bridge from DFT to effective tight-binding model)

**Purpose**: Extract effective tight-binding Hamiltonian from DFT that can:
1. Reproduce DFT band structure cheaply
2. Be twisted to model moire superlattice
3. Input into ML models for fast property prediction

**Process**:
1. Run DFT on non-twisted bilayer (e.g., aligned MoTe₂/WSe₂ at 0°)
2. Construct Wannier functions (typically 30–50 for transition metal dichalcogenides)
3. Build tight-binding Hamiltonian matrix
4. Validate: Check that TB-interpolated bands match DFT

**Moire Modulation**:
- Apply periodic potential modulation V_moire = V_0 cos(2π r/a_moire) to account for twist
- Recompute bands under moire potential (computationally cheap)
- Extract flat band structure and density of states enhancement

**Output**:
- Effective Hamiltonian matrices (exportable)
- Flat band curvature (related to effective mass enhancement)
- Density of states vs. energy (input for Boltzmann transport with moire correction)

**Computational Cost**: 
- Wannier construction: 50–200 CPU-hours per material
- Moire band sweeps (multiple twist angles): 5–20 CPU-hours per angle
- Total: ~200–500 CPU-hours for optimization

### 3.2 Machine-Learning Potential (ML Potential) for Speed

**Motivation**: DFT is expensive for exploring large composition/defect space; ML can predict properties 1000× faster

**Approach**: Train ML model (Gaussian Approximation Potential – GAP, or SNAP)

**Training data**:
- ~500–1000 DFT calculations of HEA structures
- Coverage: different compositions, temperatures (via MD trajectory snapshots), defects

**Training cost**: 
- DFT data generation: 50,000–100,000 CPU-hours
- ML model training: 1,000–5,000 CPU-hours
- One-time investment for project

**Benefit**: After training, predict energies/forces on new structures in ~1 CPU-second (vs. DFT 1–10 hours)

**Use cases**:
- Screen 100+ HEA compositions quickly
- Monte Carlo simulations of phase stability
- Molecular dynamics to explore defects, thermal properties
- Structure optimization (relax 1000 configurations in days vs. months)

---

## Level 4: Magnetic Properties – Micromagnetics (OOMMF)

### 4.1 Domain Structure & Coercivity

**Tool**: OOMMF (Object-Oriented MicroMagnetic Framework)

**Input Parameters**:
- Saturation magnetization M_s (from experiment or DFT)
- Magnetic anisotropy K_u (from SQUID torque measurements)
- Exchange stiffness A (from literature or fit to experiment)
- Damping parameter α (typical 0.01–0.1)

**Simulation**: Initialize random domain structure, relax to equilibrium, measure:
- Domain wall energy
- Coercivity H_c (switching field)
- Remanence M_r
- Domain size (typical ~100 nm)

**Computational Cost**: 
- Single domain structure: 10–50 CPU-hours (3D FFT solver)
- Parametric sweep (10 K_u values × 5 M_s values): 500–1000 CPU-hours

**Output**:
- Realistic domain configuration confirming bistability
- Estimated H_c to guide experimental pulse amplitude

### 4.2 Pulse-Driven Switching Dynamics (LLG Integration)

**Tool**: Custom OOMMF script or PyMag

**Physics**: Landau-Lifshitz-Gilbert equation (LLG):
$$\frac{d\mathbf{M}}{dt} = -\gamma \mathbf{M} \times (\mathbf{B}_{eff} + \mathbf{B}_{pulse}) + \frac{\alpha}{M_s} \mathbf{M} \times \frac{d\mathbf{M}}{dt}$$

**Simulation**:
1. Start in "down" state (remanence along -z)
2. Apply laser pulse as time-dependent magnetic field: B_pulse(t) ~ (amplitude, width, polarization)
3. Integrate LLG over 100–1000 ps
4. Check final state (did it switch to "up"?)

**Parametric study**:
- Sweep pulse amplitude A: 50–500 mT
- Sweep pulse width τ: 10–1000 ps
- Map switching probability P(A, τ) in 2D

**Computational Cost**: 
- Single pulse response: 1–10 CPU-hours (small domain <100 nm)
- Full 2D phase diagram (10×10 grid): 100–1000 CPU-hours

**Output**:
- Switching phase diagram (identify optimal pulse parameters)
- Critical amplitude A_critical, critical width τ_critical
- Comparison to experimental Kerr microscopy

---

## Level 5: Mechanical & Damage – Phase-Field / FEM

### 5.1 Thermal Stress from Thermal Cycling

**Tool**: COMSOL Multiphysics or Abaqus (commercial) or FEniCS (open-source)

**Physics**:
- Heat conduction: $\rho c \frac{\partial T}{\partial t} = \nabla \cdot (k \nabla T)$
- Elasticity: $\nabla \cdot \sigma + f = 0$
- Thermal strain: $\epsilon_{thermal} = \alpha (T - T_{ref})$ (CTE mismatch)

**Geometry**: 2D cross-section of coating layers (5 layers, each 10–100 µm thick)

**Simulation**:
1. Ramp temperature room temp → 1000°C (1°C/min)
2. Compute resulting stress tensor σ(x,y,T)
3. Compare to adhesive strength → predict delamination location
4. Cool and repeat (thermal cycling)
5. Track cumulative stress (ratcheting effect)

**Mesh**: Fine near interfaces (~1 µm), coarser in bulk (~10 µm)

**Computational Cost**: 
- Single thermal cycle: 10–50 CPU-hours (transient FEM)
- 20 cycles: 200–1000 CPU-hours

**Output**:
- Stress distribution maps at each time step
- Prediction of delamination location (highest tensile stress at interface)
- Strain energy release rate (G) vs. cycle number
- Comparison to fracture toughness (K_IC) for failure prediction

### 5.2 Self-Healing Kinetics (Phase-Field)

**Tool**: Custom phase-field code (Python + FEniCS) or COMSOL

**Physics**: Diffuse interface model of crack healing

Scalar field ϕ(x,t):
- ϕ = 0: fully healed
- ϕ = 1: fully cracked

Evolution:
$$\frac{\partial \phi}{\partial t} = M \nabla^2 \frac{\delta F}{\delta \phi} - \frac{1}{\tau_{heal}} \phi$$

Where:
- M: mobility (diffusivity in healing material)
- F: free energy (penalizes high interfaces)
- τ_heal: healing time scale (1–100 hours, fitted to experiment)

**Simulation**:
1. Initialize crack profile (width w_0 = 10–100 µm, length L = 1 mm)
2. Set boundary conditions: T = 100°C (healing temperature)
3. Time-integrate PDE until ϕ → 0 (full healing)
4. Track crack width w(t) and plot vs. time
5. Vary τ_heal to match experimental closure rate

**Computational Cost**: 
- Transient nonlinear PDE: 50–200 CPU-hours per crack geometry
- Parametric sweeps (5 initial widths × 10 τ_heal values): 2,500–10,000 CPU-hours

**Output**:
- Healing kinetics curves: w(t) comparison to optical microscopy data
- Fitted healing time constant τ_heal
- Prediction of healing efficiency η = (w_0 - w_∞) / w_0

---

## Level 6: Integrated Multi-Physics (Device Scale)

### 6.1 Coupled Thermoelectric-Magnetic-Thermal Simulation

**Tool**: COMSOL Multiphysics (built-in thermoelectric module)

**Physics**:
1. **Thermoelectric**: Apply temperature gradient ∇T → electrical current via Seebeck
2. **Joule heating**: Electrical current → dissipation (Peltier + I²R)
3. **Magnetic response**: Pulse → magnetization change ΔM → thermal signature
4. **Healing feedback**: Local temperature + damage state → healing rate

**Geometry**: Full coating cross-section, or simplified 2D model

**Simulation Protocol**:
1. Initialize with imposed ΔT (e.g., 100 K across coating)
2. Compute steady-state Seebeck voltage
3. Load pulse (B-field or strain) to induce magnetic switching
4. Track magnetization M(t) (from OOMMF output embedded as lookup table)
5. Calculate resulting Joule heat from M-induced current
6. Evolve thermal and damage fields coupled

**Computational Cost**: 
- Steady-state thermoelectric: 10–50 CPU-hours
- Transient with pulse: 100–500 CPU-hours

**Output**:
- Seebeck voltage vs. ΔT (device performance)
- Temperature increase from pulse-induced Joule heating
- Identification of hot spots (where healing preferentially occurs)
- Self-consistent multi-physics validation

---

## Implementation Roadmap

### Phase 1 (Months 1–3): DFT & Boltzmann Transport
- Goal: Screen 5–10 HEA compositions, predict optimal S and doping
- Effort: 1 PhD (DFT expert) or collaboration with theory group
- Timeline: Complete DFT by Month 2, transport optimization Month 3
- Deliverable: Transport property predictions to guide experimental synthesis

### Phase 2 (Months 2–4): Moire Band Structure
- Goal: Compute flat band structure for MoTe₂/WSe₂ at optimal twist angle
- Effort: 1 postdoc (DFT + Wannier90)
- Collaboration: Use Wannier90 training from Wien2k documentation
- Deliverable: Band structure & DOS enhancement factor

### Phase 3 (Months 3–6): Micromagnetics (LLG)
- Goal: Predict optimal pulse parameters for switching
- Effort: 1 graduate student (OOMMF learning curve ~4 weeks)
- Collaboration: Reach out to OOMMF user community, adapt example scripts
- Deliverable: Phase diagram P_switch(A, τ)

### Phase 4 (Months 4–8): Thermal Stress & Damage (FEM)
- Goal: Predict delamination locations and thermal fatigue lifetime
- Effort: 1 senior graduate student (COMSOL or FEniCS)
- Collaboration: Materials simulation center at institution (if available)
- Deliverable: Stress maps and failure prediction vs. cycle number

### Phase 5 (Months 6–10): Phase-Field Healing Kinetics
- Goal: Fit healing time constant and validate against experiment
- Effort: 1–2 graduate students (custom Python code development)
- Timeline: Parallel with experimental healing tests
- Deliverable: Closure kinetics prediction, τ_heal parameter

### Phase 6 (Months 9–12): ML Potential (Optional, High-Impact)
- Goal: Train ML model on HEA composition space for rapid screening
- Effort: 1 postdoc (ML + materials simulation background)
- Timeline: Start after 500+ DFT calculations accumulated
- Deliverable: Fast property predictor for 100+ compositions

### Phase 7 (Ongoing): Multi-Physics Integration
- Goal: Couple all scales via COMSOL
- Timeline: Start Month 6, refine throughout Year 2
- Deliverable: Integrated device simulator for design optimization

---

## Validation Against Experiment

| Prediction | Experimental Measurement | Tolerance | Timeline |
|---|---|---|---|
| **Seebeck** | ZEM measurement | ±20% (account for τ uncertainty) | Month 4 |
| **Thermal conductivity** | Laser flash | ±15% | Month 4 |
| **Domain structure** | Kerr microscopy / TEM | Qualitative (domain size order) | Month 3 |
| **Switching parameters** (A_crit, τ_crit) | Pump-probe Kerr | ±20% (varies with sample) | Month 3.5 |
| **Stress distribution** | Digital image correlation (DIC) or strain gauge | ±10% (if instrumented) | Month 6 |
| **Healing kinetics** | Optical microscopy closure tracking | ±15% (w vs. t) | Month 5 |

---

## Software Infrastructure & Version Control

### Repository Structure
```
meaqt-simulations/
├── dft/
│   ├── hea-oxide/         # VASP calculations
│   │   ├── structure.in
│   │   ├── submit.sh
│   │   └── postprocess.py (parse EIGENVAL)
│   └── moire-2d/          # DFT for MoTe₂/WSe₂
│
├── boltzmann/
│   ├── boltztrapt2.py     # BoltzTraP2 transport pipeline
│   └── results/           # S, σ, κ heatmaps
│
├── magnetic/
│   ├── oommf_scripts/     # .mif files for OOMMF
│   └── llg_solver.py      # Custom LLG integration
│
├── mechanics/
│   ├── comsol_models/     # .mph COMSOL files (or code export)
│   ├── fenics_scripts/    # FEniCS Python code
│   └── fea_mesh/          # Gmsh mesh files
│
├── healing/
│   ├── phase_field.py     # PDE solver (FEniCS-based)
│   └── kinetics_data/     # Healing curves
│
├── multiphysics/
│   ├── integrated.py      # Coupled solver (if custom)
│   └── comsol_export.m    # COMSOL live-link (if available)
│
└── data/
    ├── experiment_results/ # Link to experimental measurements
    └── validation_plots/   # Comparison DFT vs. experiment
```

### Continuous Integration (GitHub Actions)
- Auto-run DFT convergence checks on new structures
- Unit tests for Boltzmann transport pipeline
- Validation: Compare new calculations to literature benchmarks

---

## References & Tools

### Key Software (Open-Source)
- **VASP** (commercial, but widely available at institutions)
- **Quantum ESPRESSO** (free, open-source DFT)
- **BoltzTraP2** (free, GitHub: https://github.com/taserow/BoltzTraP2)
- **Wannier90** (free, Fortran)
- **OOMMF** (free, micromagnetics: https://math.nist.gov/oommf/)
- **FEniCS** (free, Python FEM: https://fenicsproject.org/)
- **COMSOL** (commercial, but trial version available)
- **Gmsh** (free, mesh generation)

### Useful References
- DFT thermoelectrics: *Reviews of Modern Physics*, Vol. 81, 2009
- Tight-binding moire systems: arXiv:2308.xxxx (search recent papers on MoTe₂/WSe₂)
- Micromagnetics: OOMMF user manual at NIST
- Phase-field healing: *Multiscale Modeling & Simulation*, Vol. 18, 2020

---

## References & Related Documents

- [Characterization Plan](CHARACTERIZATION_PLAN.md): Experimental validation targets
- [Risk Assessment](RISK_ASSESSMENT.md): Computational feasibility gates
- [dft_adapters.py](../src/meaqt/dft_adapters.py): Current DFT parsing code in project
