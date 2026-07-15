# MEAQ-T Coating: Failure Mode, Effects & Analysis (FMEA)

**Status**: Risk-based design guide  
**Last Updated**: 2026-07-15  
**Severity Scale**: 1 (minimal) – 10 (critical)  
**Likelihood Scale**: 1 (rare) – 10 (certain)  
**Detection Scale**: 1 (easy) – 10 (very difficult)

---

## FMEA Matrix Summary

| Failure Mode | Component | Severity | Likelihood | Detection | RPN | Mitigation | Status |
|---|---|---|---|---|---|---|---|
| **Delamination** | Layer interfaces | 9 | 6 | 5 | 270 | Improve interface layer, adhesion testing | In progress |
| **Thermal fatigue cracking** | Protective layer | 8 | 7 | 4 | 224 | Graded CTE, stress relief design | In progress |
| **Oxidation of 2D materials** | Moire layer | 8 | 8 | 3 | 192 | Enhanced encapsulation (50+ nm SiO₂) | In progress |
| **HEA phase separation** | Interlayer | 7 | 5 | 6 | 210 | Optimize sintering, limit dwell time | Design review |
| **Healing saturation** | Vitrimer layer | 6 | 4 | 7 | 168 | Re-heal cycles, higher healing temp | Testing |
| **Seebeck reduction** | Moire layer | 7 | 6 | 4 | 168 | Optimize twist angle, doping | Optimization |
| **Magnetic state instability** | Moire layer | 8 | 5 | 6 | 240 | Stronger anisotropy, bias field | Design review |
| **Adhesion loss after cycling** | Interfaces | 8 | 6 | 5 | 240 | Strengthen bonds, use interlayer | In progress |
| **Radiation-induced defects** | All layers | 7 | 3 | 8 | 168 | Radiation-hardened materials, annealing | Future work |
| **Corrosion/oxidation** | Protective layer | 6 | 4 | 7 | 168 | Ceramic top coat, sealed edges | Testing |

---

## Detailed Failure Mode Analysis

---

### **FM-1: Delamination at Layer Interfaces**

**Location**: Protective/HEA, HEA/compliance, compliance/moire boundaries

**Severity**: 9 (loss of all functionality, safety hazard potential)

**Root Causes**:
1. Inadequate surface cleaning before layer deposition
2. Thermal mismatch (CTE difference >5 ppm/K) causing tensile stress during thermal cycling
3. Weak interfacial bonding (adhesion <5 MPa)
4. Contamination or moisture at interface during deposition

**Mechanism**:
- Stress accumulates at interface during thermal cycling
- Shear stress exceeds adhesive strength
- Progressive debonding initiates from edges/defects
- Rapid propagation once initiated (catastrophic failure)

**Detection Methods**:
- Acoustic microscopy (ultrasonic imaging) – Detects voids
- Scanning electron microscopy cross-section – Direct visual
- Peel strength testing (destructive)
- Thermal imaging during thermal shock – Delamination shows as hot spot

**RPN**: **270** (HIGH RISK)

**Mitigation Strategies**:

1. **Improve adhesion**
   - Use graded interface layer (3-layer CTE gradient)
   - Target adhesion strength: σ_pull > 10 MPa (vs. 5 MPa baseline)
   - Application: Implement compliance layer as described in Synthesis Protocol

2. **Reduce thermal stress**
   - Match CTEs within ±1 ppm/K if possible
   - Design cooling ramps ≤2°C/min to avoid thermal shock
   - Use stress-relief anneals between layer additions

3. **Quality control**
   - Pre-coating SEM inspection of substrate surface
   - Adhesion pull-test on witness samples (1 per batch)
   - Acoustic microscopy of ≥50% of produced coatings

4. **Material substitution** (if needed)
   - Replace rigid protective layer with elastomeric vitrimer (lower modulus → less stress)
   - Use SiC-based HEA instead of oxide HEA (better CTE match)

**Success Metric**: Zero delamination observed after 20 thermal cycles (room temp ↔ 1000°C)

**Timeline**: Implement mitigation by Month 3 (prototype phase)

---

### **FM-2: Thermal Fatigue Cracking of Protective Layer**

**Location**: Surface and through-thickness of protective coating

**Severity**: 8 (loss of protection, exposure of underlying layers)

**Root Causes**:
1. High residual tensile stress from differential shrinkage during cooling
2. Rapid thermal transients (thermal shock: ΔT > 500 K in <1 min)
3. Low fracture toughness of monolithic ceramic (e.g., HfB₂ without reinforcement)
4. Pre-existing defects or manufacturing flaws

**Mechanism**:
- Protective layer heated to T_service
- Sudden cooling (e.g., loss-of-coolant accident) induces tensile stress
- Stress exceeds critical stress intensity (K_IC) → crack initiation
- Cracks propagate through coating in minutes

**Detection Methods**:
- Visual inspection (through-coating optical measurement)
- Thermal imaging during thermal cycling (cracks visible as local hot spots)
- SEM cross-section (post-mortem)
- Acoustic emission monitoring (during cycling)

**RPN**: **224** (HIGH RISK)

**Mitigation Strategies**:

1. **Design for stress relief**
   - Introduce microporosity (~5–10%) → compliance, reduced stress
   - Use whisker-reinforced composites (SiC whiskers, 5–10 wt%)
   - Thickness grading: thicker at center, taper toward edges

2. **Material toughening**
   - Replace monolithic HfB₂ with HfB₂-SiC composite (K_IC increase 2–3×)
   - Add graphene platelets (2–5 wt%) for crack bridging

3. **Operational procedures**
   - Limit thermal ramp rate: ≤2°C/min heating, ≤5°C/min cooling
   - Avoid rapid thermal transients (e.g., emergency quenching)
   - Use thermal buffers (intermediate cooling reservoirs)

4. **Process optimization**
   - Optimize sintering to minimize residual stress
   - Slow cooling from sinter temperature (furnace cool, not water quench)
   - Post-sinter stress-relief anneal at 70% of sinter temp, 2 h

**Success Metric**: No through-cracks after 50 thermal cycles (500 K ΔT, 2°C/min ramp)

**Timeline**: Implement material upgrade by Month 4 (prototype optimization)

---

### **FM-3: Oxidation of 2D Materials (Moire Layer)**

**Location**: MoTe₂, WSe₂ heterostructure under protective layer

**Severity**: 8 (complete loss of moire transport and magnetic features)

**Root Causes**:
1. **Incomplete encapsulation**: SiO₂ coverage <50%, gaps in top layer
2. **Oxygen permeation**: Through cracks in protective or SiO₂ layer during thermal cycling
3. **Interface oxidation**: Grain boundaries allow O₂ diffusion
4. **Moisture ingress**: Hygroscopic vitrimer layer absorbs water, enabling electrochemical oxidation

**Mechanism**:
- O₂ reaches 2D material surface through defects
- Oxidation: MoTe₂ + 2O₂ → MoO₃ + TeO₂ (irreversible)
- Process accelerated at elevated temperature (T > 200°C)
- Loss of metallicity, transport properties → Seebeck, magnetization destroyed

**Detection Methods**:
- Raman spectroscopy (A₁g and E' peaks broaden and disappear upon oxidation)
- SEM/EDS (oxygen spike at layer location post-thermal aging)
- Electrical conductivity measurement (σ drops by orders of magnitude)
- X-ray photoelectron spectroscopy (XPS) – Direct oxidation state measurement

**RPN**: **192** (MODERATE-HIGH RISK)

**Mitigation Strategies**:

1. **Enhance encapsulation**
   - Increase SiO₂ or Al₂O₃ encapsulation thickness: 50 nm → 100–200 nm
   - Deposit via atomic layer deposition (ALD) for pinhole-free coverage
   - Verify coverage with SEM cross-section (target >99%)

2. **Reduce operating temperature**
   - Design for T_service < 150°C (oxidation kinetics much slower)
   - If high-temp operation required, use inert atmosphere or hermetic sealing

3. **Material substitution**
   - Replace vitrimer with silicate binder (less moisture uptake)
   - Use graphene as encapsulant (impermeable to O₂)

4. **Environmental control**
   - Store coatings in dry (RH <30%) and inert (Ar or N₂) atmosphere
   - Hermetic packaging for shipped samples

5. **Accelerated testing for validation**
   - Age samples at 250°C in air for 168 h (equivalent to years at room temp)
   - Measure Seebeck & Raman before/after
   - Success: <10% drop in Seebeck coefficient

**Success Metric**: No Raman peak shifts, <5% conductivity change after 500 h at 150°C in air

**Timeline**: Implement by Month 6 (scale-up phase)

---

### **FM-4: HEA Phase Separation & Phase Instability**

**Location**: High-entropy interlayer (Hf, Zr, Ta, Nb, Ti)O

**Severity**: 7 (partial loss of thermal stability, reduced healing potential)

**Root Causes**:
1. **Insufficient entropy**: Configurational entropy S_mix < 1.4 R (edge of HEA regime)
2. **High sintering temperature**: >1500°C promotes atomic diffusion → phase ordering
3. **Long dwell times**: >3 h at peak temperature → kinetic ordering
4. **Oxygen partial pressure**: Reduced P_O₂ → preferential oxidation of elements

**Mechanism**:
- At high temperature, entropic driving force weakens (ΔG = ΔH - T·ΔS → favors ΔH term)
- Atomic diffusion activates (D ∝ exp(-E_a/k_B T))
- System gradually orders into lower-entropy phases
- Result: Multi-phase mixture (less stable, lower hardness, reduced healing capacity)

**Detection Methods**:
- X-ray diffraction (XRD) before/after thermal aging (peak splitting indicates ordering)
- Transmission electron microscopy (TEM) – Direct phase imaging
- Calorimetry (phase transitions reveal as DSC peaks)
- Nanohardness mapping (phase-specific hardness variation)

**RPN**: **210** (MODERATE-HIGH RISK)

**Mitigation Strategies**:

1. **Optimize sintering conditions**
   - Lower peak temperature: 1400°C → 1300°C (reduces diffusion)
   - Shorten dwell: 2 h → 1 h at peak (reduces ordering time)
   - Faster cooling: >5°C/min post-sinter (quench-locks high-entropy phase)

2. **Composition fine-tuning**
   - Increase S_mix target: 1.5 R → 1.8 R (add more elements or change ratios)
   - Add entropy-stabilizing element (e.g., rare earth or Al)
   - Perform computational CALPHAD screening to predict stable phases

3. **Control oxygen stoichiometry**
   - Sinter in Ar or forming gas (reduce P_O₂)
   - Avoid prolonged air exposure pre-sintering

4. **Post-sinter verification**
   - XRD on every 5th sample (batch QC)
   - If phase separation detected, re-optimize sintering parameters

**Success Metric**: Single-phase XRD pattern after sintering and 1000 h at 1000°C

**Timeline**: Optimization by Month 2 (early-stage)

---

### **FM-5: Healing Saturation / Repeated Healing Failure**

**Location**: Bio-vitrimer protective/healing layer

**Severity**: 6 (loss of self-healing capability after 3–5 cycles)

**Root Causes**:
1. **Cross-link exhaustion**: Reversible cross-links (imine or transesterification) mechanically break and cannot reform
2. **Polymer chain scission**: UV or thermal degradation breaks backbone
3. **Insufficient healing material**: Vitrimer concentration too low to refill cracks
4. **Healing temperature instability**: Fluctuating T during healing → inconsistent rate

**Mechanism**:
- First healing cycle: 80–120°C allows cross-link exchange, closure
- Repeated heating weakens polymer network
- After 3–5 cycles: Cross-link density sufficiently reduced that network no longer flows
- Subsequent cracks cannot close → healing fails

**Detection Methods**:
- Resistance monitoring during healing (ΔR/R_initial should trend to 0; saturation shows asymptote)
- Optical microscopy (visual crack closure tracking; slowdown after N cycles)
- Mechanical testing (flexural strength post-healing)
- Thermal gravimetric analysis (TGA) – Mass loss indicating chain scission

**RPN**: **168** (MODERATE RISK)

**Mitigation Strategies**:

1. **Optimize healing formulation**
   - Increase cross-link density initially: 1.5× more reactive groups
   - Use **supramolecular healing**: hydrogen bonds + covalent cross-links
   - Add microcapsules of liquid healing agent (backup supply)

2. **Optimize healing temperature**
   - Sweet spot: 100–120°C (allows cross-link exchange without side reactions)
   - Avoid >150°C (accelerates thermal degradation)
   - Consider **multi-step healing**: gentle warm (60°C) for 12 h, then high-temp (120°C) for 2 h

3. **Limit cycle duty**
   - Design for 3–5 healing cycles maximum
   - Include "healing history" tracking (after Nth cycle, accept permanent damage)
   - If more cycles needed: replace coating section or entire coat

4. **Material alternatives**
   - Investigate PDMS-based vitrimers (higher cycle count reported: >10 cycles)
   - Test thermoplastic elastomers (unlimited thermal healing via melting)

**Success Metric**: >80% crack closure for 5 consecutive healing cycles, with <20% loss in closure fraction

**Timeline**: Formulation optimization by Month 5 (scale-up phase)

---

### **FM-6: Reduced Seebeck Coefficient (Transport Degradation)**

**Location**: Moire layer (MoTe₂/WSe₂ heterostructure)

**Severity**: 7 (primary function loss)

**Root Causes**:
1. **Suboptimal twist angle**: Off-resonance moire condition (flat bands not achieved)
2. **Insufficient filling control**: Carrier concentration away from optimal doping
3. **Impurity scattering**: Residual contamination in 2D material (oxygen, polymer residues)
4. **Disorder in moire superlattice**: Imperfect stacking, rotational misalignment

**Mechanism**:
- Seebeck coefficient ∝ entropy per carrier (S ∝ (k_B/e) × ln[(E-E_F) / k_B T])
- Optimal S achieved near band edge (low density-of-states)
- If moire band structure poorly formed → less enhanced DOS
- Insufficient filling → not enough carriers to sample band edge
- Result: S_measured < 100 µV/K (vs. target >100 µV/K)

**Detection Methods**:
- Seebeck measurement across temperature (extract magnitude & sign)
- Raman spectroscopy (peak positions indicate disorder)
- STM/STS (map local DOS and verify moire pattern)
- Electrical conductivity measurement (check carrier concentration)

**RPN**: **168** (MODERATE RISK)

**Mitigation Strategies**:

1. **Fine-tune twist angle**
   - Theoretical prediction: θ_optimal ≈ 1.1° for MoTe₂/WSe₂
   - Experimental optimization: Produce samples at θ = {0.9°, 1.0°, 1.1°, 1.2°, 1.3°}
   - Measure Seebeck for each, identify peak

2. **Doping optimization**
   - Apply controlled gate voltage (via backgate or top gate)
   - Sweep gate voltage, measure S vs. V_g
   - Identify optimal filling factor (n* or p*)
   - For prototype: Focus on highest-S configuration

3. **Improve 2D material quality**
   - Source higher-purity MoTe₂ & WSe₂ flakes (mechanical exfoliation preferred over CVD for prototypes)
   - Extend vacuum anneal during transfer: 250°C, 1 h
   - Verify with Raman linewidth (target FWHM < 4 cm⁻¹)

4. **Design review**
   - Revisit Boltzmann transport model (composition.py, moire_transport.py)
   - Calibrate against literature data (measure Seebeck on reference samples)
   - Validate moire band structure assumptions with DFT

**Success Metric**: Seebeck coefficient >100 µV/K in optimal twist/doping condition

**Timeline**: Optimization by Month 3 (prototype characterization phase)

---

### **FM-7: Magnetic State Instability**

**Location**: Moire layer (interfacial magnetism)

**Severity**: 8 (loss of pulse-switchable magnetization)

**Root Causes**:
1. **Weak magnetic anisotropy**: K_u < 10⁴ erg/cm³ (insufficient to stabilize states)
2. **Thermal fluctuations**: k_B T comparable to anisotropy energy → stochastic switching
3. **Insufficient bias field**: H_bias too weak to maintain state between pulses
4. **Interfacial roughness**: Disorder reduces anisotropy

**Mechanism**:
- Magnetic bistability requires anisotropy energy E_anis = K_u V >> k_B T
- If K_u too weak: E_anis ≈ k_B T → Boltzmann statistics → random state hops
- Bias field prevents stable ± states
- Pulse-driven switching becomes probabilistic (low switching probability P_switch)

**Detection Methods**:
- SQUID magnetometry (measure K_u from torque curves)
- PPMS magnetic field sweep (measure coercivity H_c and bistability)
- Time-resolved Kerr (assess switching probability P_switch vs. pulse amplitude)
- Thermal stability measurement (hold at T, monitor spontaneous demagnetization rate)

**RPN**: **240** (HIGH RISK)

**Mitigation Strategies**:

1. **Enhance interfacial anisotropy**
   - Interface engineering: Optimize Fe/TiO₂ (or similar) thickness
   - Perpendicular magnetic anisotropy (PMA) materials: Co/Ni multilayers
   - Theoretical prediction: K_u scales with interface quality (Rashba spin-orbit coupling)
   - Target: K_u > 10⁵ erg/cm³

2. **Increase bias magnetic field**
   - Integrate permanent magnet (NdFeB) nearby (H_bias ≈ 0.1–0.5 T)
   - Use thin interlayer of ferrimagnetic material (e.g., Y₃Fe₅O₁₂) for exchange bias

3. **Material substitution**
   - Replace MoTe₂/WSe₂ with **materials having intrinsic magnetism**: Cr₂Ge₂Te₆, CrI₃
   - These 2D ferromagnetic materials have stronger K_u (easier to control)

4. **Operational constraints**
   - Limit service temperature: T_service < 0.3 × T_C (Curie temperature)
   - Avoid prolonged exposure to stray magnetic fields

**Success Metric**: Switching probability P_switch > 70%, stable states persisting >1 h without re-excitation

**Timeline**: Material upgrade or engineering redesign by Month 3–4

---

### **FM-8: Adhesion Loss After Thermal Cycling**

**Location**: Layer interfaces (all four)

**Severity**: 8 (coating delamination, loss of all function)

**Root Causes**:
1. **Cumulative tensile stress**: Each thermal cycle adds residual stress
2. **Ratcheting**: Creep under tensile stress during heating, incomplete elastic recovery on cooling
3. **Interface reactions**: High-temp reactions weaken bonds over time
4. **Crack initiation at stress concentrators**: Defects grow per cycle

**Mechanism**:
- Cycle 1: Stress accumulates, but below failure threshold
- Cycles 2–10: Stress ratchets up each cycle (plastic deformation + creep)
- Cycle N: Stress exceeds adhesive strength → sudden delamination

**Detection Methods**:
- Ultrasonic (acoustic impedance mismatch detects delamination)
- Thermal imaging (delaminated areas show higher temperature in transient heating)
- Mechanical testing (peel/pull strength decreases cycle-by-cycle)
- SEM cross-section post-cycling

**RPN**: **240** (HIGH RISK)

**Mitigation Strategies**:

1. **Reduce cumulative stress**
   - Stress-relief layers: Introduce compliant (low-modulus) interlayers
   - Graded CTE: Design 3–5 layer grading to minimize ΔT-induced stress
   - Thinner films: Reduce absolute stress (σ ∝ t × E)

2. **Strengthen interfaces**
   - Surface roughening before each layer (sand, grit blast)
   - Chemical adhesion promoters (silanes, coupling agents)
   - Higher sintering/bonding temperatures (within material limits)

3. **Modify stress state**
   - Apply compressive pre-stress (shot peening of protective layer)
   - Residual compression buffers subsequent tensile stress

4. **Limit cycle duty**
   - Design for specific number of cycles (e.g., 20 cycles guaranteed)
   - Preventive replacement before reaching limit

**Success Metric**: Adhesion strength maintained >50% of initial value after 20 thermal cycles (room temp ↔ 1200°C)

**Timeline**: Interface strengthening by Month 4 (prototype optimization)

---

### **FM-9: Radiation-Induced Defects**

**Location**: All layers (especially HEA interlayer and 2D layer)

**Severity**: 7 (property degradation in high-radiation environments)

**Root Causes**:
1. **High-energy particle interactions**: Knockon defects from neutrons, protons, or heavy ions
2. **Defect accumulation**: Vacancies and interstitials reduce carrier mobility, thermal conductivity
3. **Transmutation**: High neutron flux → nuclear reactions create new elements (alloying effect)
4. **Amorphization**: Severe irradiation can amorphize crystalline layers

**Mechanism**:
- Incident particle imparts energy to lattice atoms
- Atom displaced if energy > displacement threshold (~25 eV for oxides)
- Cascading displacements create fault regions
- Defects scatter carriers, phonons → reduced σ, κ, S

**Detection Methods**:
- Raman (peak broadening, downshift with defects)
- TEM (point defect and dislocation imaging)
- Positron annihilation spectroscopy (vacancy detection)
- Transport measurement pre/post-irradiation

**RPN**: **168** (MODERATE RISK, design-specific)

**Mitigation Strategies**:

1. **Material selection for radiation hardness**
   - High-Z elements more resistant (e.g., Hf, Zr vs. Ti)
   - Carbides more robust than oxides (HfB₂ > HfO₂)
   - Use known radiation-hard ceramics: SiC, Al₂O₃

2. **Design-in redundancy**
   - Thicker protective layer (absorbs some damage before reaching active layer)
   - Multiple independent paths for function (parallel 2D stacks?)

3. **Annealing to recover**
   - Periodic thermal annealing at high temp (80% of T_melt for ~1 h) annihilates defects
   - Integrate into maintenance schedule for high-radiation service

4. **Operational limits**
   - Document dose limits (e.g., "maintains ZT > 0.1 up to 10¹⁹ cm⁻² fluence")
   - Recommend preemptive replacement at specified dose

**Success Metric**: <20% degradation in κ, σ, S after 10¹⁸ cm⁻² (1 MeV equivalent) neutron fluence

**Timeline**: Radiation testing & mitigation by Month 8–12 (advanced validation phase)

---

### **FM-10: Corrosion & Oxidation in Aggressive Environments**

**Location**: Protective layer surface and grain boundaries

**Severity**: 6 (gradual loss of protection, eventual core exposure)

**Root Causes**:
1. **Oxygen ingress**: Through grain boundaries or micro-cracks
2. **Aqueous corrosion**: Salt spray, moisture → electrochemical attack
3. **Acid/base attack**: Chemical dissolving of protective layer
4. **Galvanic corrosion**: Differential electrochemical potential between layers/substrate

**Mechanism**:
- O₂ + 4e⁻ + 2H₂O → 4OH⁻ (cathodic reaction)
- Metal/oxide → Metal^n+ + ne⁻ (anodic reaction, if substrate exposed)
- Net: Preferential corrosion at defects or high-energy sites

**Detection Methods**:
- Visual inspection + light microscopy (rust staining, pitting)
- Electrochemical impedance spectroscopy (EIS) – Porosity & corrosion rate
- Salt spray testing (ASTM B117, 500–1000 h)
- Mass loss measurement (before/after immersion)

**RPN**: **168** (MODERATE RISK)

**Mitigation Strategies**:

1. **Seal edges & defects**
   - Perimeter sealant (epoxy or polyimide) around coating
   - Eliminate open porosity in protective layer

2. **Enhance protective layer**
   - Thickness: 100 µm → 200+ µm (longer diffusion path for O₂)
   - Add hydrophobic topcoat (wax, silicone) to reduce water ingress
   - Use more chemically stable materials (e.g., MgAl₂O₄, diamond-like carbon topcoat)

3. **Sacrificial layer (cathodic protection)**
   - Embed reactive metal (Zn or Mg) at edges as sacrificial anode
   - Preferential oxidation of sacrificial layer protects substrate

4. **Operational measures**
   - Store in dry environment (RH <40%)
   - Regular inspection schedule
   - Preventive re-coating after 1–2 years in salt spray environments

**Success Metric**: <1% area loss after 500 h salt spray (ASTM B117); <5 mm² pitting

**Timeline**: Enhancement by Month 6 (durability testing phase)

---

## Summary Risk Matrix (RPN Ranking)

| Rank | Failure Mode | RPN | Priority |
|------|---|---|---|
| 1 | Delamination | 270 | **CRITICAL** – Address Month 1–2 |
| 2 | Magnetic state instability | 240 | **CRITICAL** – Address Month 2–3 |
| 3 | Adhesion loss after cycling | 240 | **CRITICAL** – Address Month 2–3 |
| 4 | Thermal fatigue cracking | 224 | **HIGH** – Address Month 3–4 |
| 5 | HEA phase separation | 210 | **HIGH** – Address Month 1–2 |
| 6 | Oxidation of 2D materials | 192 | **MODERATE-HIGH** – Address Month 3–4 |
| 7 | Reduced Seebeck | 168 | **MODERATE** – Address Month 3 |
| 8 | Healing saturation | 168 | **MODERATE** – Address Month 4–5 |
| 9 | Radiation defects | 168 | **MODERATE** – Address Month 8+ |
| 10 | Corrosion | 168 | **MODERATE** – Address Month 5–6 |

---

## Action Plan Timeline

**Phase 1 (Months 1–2): Critical Risk Reduction**
- Improve interface adhesion (FM-1)
- Optimize HEA phase stability (FM-4)
- Begin magnetic state stabilization (FM-7)

**Phase 2 (Months 3–4): High-Risk Mitigation**
- Thermal fatigue testing & design (FM-2)
- Enhanced 2D material encapsulation (FM-3)
- Fine-tune Seebeck & magnetic switching (FM-6, FM-7)

**Phase 3 (Months 5–6): Durability Qualification**
- Thermal cycling endurance (FM-8)
- Healing cycle optimization (FM-5)
- Corrosion testing (FM-10)

**Phase 4 (Months 8+): Advanced Environment**
- Radiation hardness validation (FM-9)
- Long-term aging studies
- Failure documentation & design fixes

---

## References & Related Documents

- [Synthesis Protocol](SYNTHESIS_PROTOCOL.md) – How to avoid manufacturing defects
- [Characterization Plan](CHARACTERIZATION_PLAN.md) – How to detect failures early
- [Risk Assessment](RISK_ASSESSMENT.md) – Go/no-go gates tied to FMEA results
