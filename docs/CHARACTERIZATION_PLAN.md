# MEAQ-T Coating: Characterization & Validation Plan

**Status**: Research roadmap for experimental validation  
**Last Updated**: 2026-07-15

---

## Executive Summary

This document outlines the **multi-scale characterization strategy** to validate MEAQ-T coating performance across five objective pillars:
1. **Thermoelectric response** (Seebeck, conductivity, power factor)
2. **Magnetic switchability** (pulse-driven state control, reversibility)
3. **Thermal robustness** (phase stability, conductivity under thermal stress)
4. **Self-healing kinetics** (crack closure rate, property recovery)
5. **Extreme-environment survivability** (radiation hardness, corrosion resistance)

---

## Tier 1: Initial Characterization (Feasibility Proof, ~2 months)

### 1.1 Morphology & Composition

**Objective**: Confirm layer integrity, thickness, and elemental distribution

| Test | Technique | Target | Equipment | Cost | Timeline |
|------|-----------|--------|-----------|------|----------|
| Layer thickness | SEM cross-section | ±5 µm accuracy | SEM | $50–100/hr | 1 week |
| Elemental map | EDS (SEM-attached) | Uniform distribution, no segregation | SEM + EDS | $100–150/hr | 1 week |
| Phase identification | XRD powder diffraction | Single-phase HEA or known second phases | XRD lab | $50–100/sample | 2 weeks |
| Surface topology | AFM or optical profiler | Roughness Ra < 5 nm | AFM/profilometer | $100–200/hr | 1 week |
| 2D material quality | Raman spectroscopy | Sharp, well-defined peaks for MoTe₂, WSe₂ | Raman lab | $80–150/sample | 1 week |

### 1.2 Thermal Properties

**Objective**: Establish baseline thermal conductivity, CTE mismatch, thermal stability

| Test | Technique | Target | Equipment | Cost | Timeline |
|------|-----------|--------|-----------|------|----------|
| Thermal conductivity | Laser flash analysis (LFA) | κ = 1–3 W/m-K for HEA, <0.5 W/m-K for healing layer | LFA instrument | $200–300/sample | 2 weeks |
| Specific heat capacity | DSC (differential scanning calorimetry) | Cp values for coating stack | DSC instrument | $150–200/sample | 2 weeks |
| Thermal expansion | TMA (thermomechanical analysis) | CTE mismatch quantification | TMA instrument | $100–150/sample | 2 weeks |
| Melting point | DSC or optical heating | Confirm no phase transitions in service window | DSC/high-temp microscope | $200–300/sample | 2 weeks |

### 1.3 Mechanical & Adhesion

**Objective**: Establish baseline mechanical robustness and layer bonding

| Test | Technique | Target | Equipment | Cost | Timeline |
|------|-----------|--------|-----------|------|----------|
| Hardness (bulk layer) | Vickers or Knoop indentation | HV = 800–2000 for HEA, <500 for protective | Hardness tester | $50–100/sample | 1 week |
| Adhesion (layer-to-layer) | Pull-off adhesion test (ASTM D4541) | σ_adhesion > 5 MPa | Adhesion testing rig | $150–250/sample | 2 weeks |
| Scratch resistance | Scratch test (ASTM C1624) | Critical load Lc > 50 mN | Scratch tester | $100–150/sample | 1 week |
| Thermal shock resistance | Rapid thermal cycling | 5–10 cycles: room temp ↔ 1200°C, assess cracking | High-temp furnace | $50–100/cycle | 2 weeks |

---

## Tier 2: Transport Characterization (Thermoelectric Validation, ~3 months)

### 2.1 Electrical Transport

**Objective**: Measure and map Seebeck coefficient, electrical conductivity across temperature and field

| Test | Technique | Target | Equipment | Cost | Timeline |
|------|-----------|--------|-----------|------|----------|
| **Seebeck coefficient** (T-dependent) | ZEM-3 or PPMS thermal transport | S = 50–200 µV/K in optimal regime | ZEM or PPMS | $2000–4000/sample | 4 weeks |
| **Electrical conductivity** (T-dependent) | 4-point probe or PPMS | σ_opt ≈ 100–500 S/cm (dependent on doping) | 4-point probe/PPMS | $1500–3000/sample | 4 weeks |
| **Power factor** (calculated) | P = σ × S² | Target: 1–5 µW/cm-K² | Derived from σ & S | Calculated | Parallel |
| **Charge carrier concentration** | Hall effect (PPMS) | n or p >> 10¹⁹ cm⁻³ | PPMS with Hall probe | $2000–3000/sample | 3 weeks |

### 2.2 Thermal Transport

**Objective**: Measure lattice and electronic thermal conductivity contributions

| Test | Technique | Target | Equipment | Cost | Timeline |
|------|-----------|--------|-----------|------|----------|
| **Total thermal conductivity** | LFA (vs. temperature) | κ_total ≈ 2–5 W/m-K at 300 K | LFA instrument | $300–500/sample | 3 weeks |
| **Thermal conductivity decomposition** | κ_e from Wiedemann-Franz law | κ_lattice = κ_total - κ_e | Derived analysis | Calculated | Parallel |
| **Thermal diffusivity** | LFA (direct measurement) | α ≈ 1–10 mm²/s | LFA | $300–500/sample | 3 weeks |

### 2.3 Figure of Merit (ZT)

**Calculation**:
$$ZT = \frac{S^2 \sigma T}{\kappa} = \frac{(\text{power factor}) \times T}{\kappa}$$

**Target**: ZT_eff > 0.1–0.3 in optimal moire regime (prototype goal)

---

## Tier 3: Magnetic Characterization (Pulse Switching Validation, ~2 months)

### 3.1 Static Magnetic Properties

**Objective**: Establish baseline magnetization, anisotropy, domain structure

| Test | Technique | Target | Equipment | Cost | Timeline |
|------|-----------|--------|-----------|------|----------|
| **Saturation magnetization** | SQUID or VSM | M_s ≈ 100–500 emu/cm³ (dependent on composition) | SQUID or VSM | $1000–2000/sample | 2 weeks |
| **Magnetic anisotropy energy** | Torque magnetometry or SQUID | K_u > 10⁵ erg/cm³ (ensures bistability) | SQUID with torque | $1500–3000/sample | 2 weeks |
| **Coercivity** (remnant field) | VSM or SQUID | H_c ≈ 100–1000 Oe (state stability) | VSM/SQUID | $800–1500/sample | 2 weeks |
| **Domain structure** | Kerr microscopy or Lorentz TEM | Stripe/vortex domains visible, <1 µm size | Kerr or TEM | $3000–5000/sample | 3 weeks |

### 3.2 Pulse-Driven Switching (Pump-Probe Experiments)

**Objective**: Demonstrate reversible magnetization switching and assess switching fidelity

| Test | Technique | Target | Equipment | Cost | Timeline |
|------|-----------|--------|-----------|------|----------|
| **Pulse-induced magnetization reversal** | Time-resolved Kerr microscopy + femtosecond laser | Deterministic switching probability > 50% | Pump-probe laser system | $10,000–20,000/day rental | 3 weeks |
| **Switching time** | TR-MOKE (time-resolved magnetic optical Kerr) | τ_switch < 100 ps | Femtosecond laser + photodiode | $5000–10,000/day | 3 weeks |
| **Threshold pulse amplitude/width** | Phase diagram (2D sweep) | Map switching boundary in (amplitude, width) space | Pulse generator + optical setup | $2000–5000 | 4 weeks |
| **Cycle endurance** | Repeated switching at fixed pulse | No degradation after 10⁶ cycles | Automated pulse train | $3000–5000 | 2 weeks |

### 3.3 Topological Charge & Skyrmion Dynamics (Advanced)

**Objective**: Assess if switching involves topological spin textures (skyrmions)

| Test | Technique | Target | Equipment | Cost | Timeline |
|------|-----------|--------|-----------|------|----------|
| **Real-space skyrmion imaging** | Lorentz TEM or spin-polarized STM | Confirmed skyrmion lattice (optional, if observed) | TEM/STM facility | $5000–10,000/sample | 4 weeks |
| **Hall conductivity (AHE)** | PPMS Hall probe | Anomalous Hall effect signature ∝ skyrmion density | PPMS | $1500–3000 | 2 weeks |
| **Topological charge calculation** | Q = ∫∫ (m · (∂m/∂x × ∂m/∂y)) dA dx dy | Q ≈ ±1 if skyrmions present, 0 if ferromagnetic | From Kerr/TEM data | Calculated | Parallel |

---

## Tier 4: Durability & Healing (Long-term Validation, ~4 months)

### 4.1 Crack Initiation & Healing Kinetics

**Objective**: Quantify self-healing efficiency and recovery timeline

| Test | Technique | Target | Equipment | Cost | Timeline |
|------|-----------|--------|-----------|------|----------|
| **Controlled crack introduction** | Three-point bend + controlled fracture | Reproducible microcrack depth 5–50 µm | Mechanical testing rig | $500–1000 | 1 week |
| **Optical tracking of closure** | Optical microscopy + image analysis | Crack width vs. time at healing temperature | Microscope + heating stage | $200–500/sample | 3 weeks |
| **Electrical property recovery** | Resistance measurement during healing | ΔR/R_initial → 0 as healing progresses | 4-point probe + furnace | $300–600/sample | 2 weeks |
| **Healing efficiency** | Calculated from closure fraction | η_heal = (w_initial - w_final) / w_initial > 80% | Data analysis | $0 | Parallel |

### 4.2 Thermal Cycling & Fatigue

**Objective**: Assess durability under repeated thermal stress

| Test | Technique | Target | Equipment | Cost | Timeline |
|------|-----------|--------|-----------|------|----------|
| **Thermal fatigue** | Rapid thermal cycling (ΔT ≈ 1000 K) | No delamination after 10–50 cycles | Thermal cycling furnace | $100–200/cycle | 4 weeks |
| **Residual stress evolution** | X-ray diffraction (peak shift) | Stress relaxation as healing occurs | XRD lab | $150–300/sample | 2 weeks |
| **Property retention** | Re-measure κ, σ, S after cycling | <20% change in transport properties | Transport labs | $1500–3000 | 2 weeks |

### 4.3 Corrosion & Chemical Attack

**Objective**: Evaluate protective layer durability in aggressive environments

| Test | Technique | Target | Equipment | Cost | Timeline |
|------|-----------|--------|-----------|------|----------|
| **Salt spray (ASTM B117)** | 500 h exposure to 5% NaCl fog | No coating failure, minimal color change | Salt spray chamber | $150–300 | 3 weeks |
| **Oxidation resistance** | High-temperature air furnace | 1000 h at 1000°C, <1% mass change | High-temp furnace | $200–400 | 5 weeks |
| **Acid/base immersion** | 72 h immersion in 1 M HCl or NaOH | Surface etching <10 µm | Chemical bath | $50–100 | 1 week |

---

## Tier 5: Extreme-Environment Testing (Specialized, ~6 months)

### 5.1 Radiation Hardness

**Objective**: Assess performance under high-energy particle flux

| Test | Technique | Target | Equipment | Cost | Timeline |
|------|-----------|--------|-----------|------|----------|
| **Ion beam irradiation** | 1 MeV electrons or protons, fluence 10¹⁸–10²⁰ cm⁻² | <10% change in κ, σ after irradiation | Ion beam facility | $5000–15,000 | 4–6 weeks |
| **Defect density mapping** | TEM or Raman after irradiation | Quantify point defects, dislocations | TEM/Raman | $2000–5000 | 2 weeks |
| **Recovery annealing** | Isochronal or isothermal annealing post-irradiation | Property restoration vs. temperature | Furnace + measurement | $1000–2000 | 2 weeks |

### 5.2 Radiation-Induced Healing

**Objective**: Novel aspect—can radiation-generated defects facilitate healing?

| Test | Procedure | Expected Outcome | Cost |
|------|-----------|------|------|
| Introduce controlled defects via ion beam | Irradiate to 10¹⁸ cm⁻² (low dose) | Defect-mediated healing channel activated | $3000–5000 |
| Measure crack closure with defects | Heat-and-monitor cracks | Closure faster than un-irradiated baseline | $500–1000 |

---

## Tier 6: In-Situ / Operando Measurements (Real-World Validation, Ongoing)

### 6.1 Temperature-Dependent Transport in Designed Geometry

**Objective**: Measure Seebeck under actual thermal gradient (not isothermal)

| Setup | Target | Timeline |
|-------|--------|----------|
| **Seebeck measurement with controlled ∇T** | Measure S_eff under true thermal gradient | 2–3 weeks per temperature point |
| **Power generation prototype** | Integrate coated sample into small thermoelectric generator | Demonstrate mW-level power output | 6–8 weeks |

### 6.2 Pulse Response in Integrated Device

**Objective**: Demonstrate pulse-driven state control in a real coating on substrate

| Experiment | Goal | Timeline |
|-----------|------|----------|
| Apply laser pulses to coated coupon | Optical pump-probe, measure magnetization response | 2–3 weeks |
| Track recovery between pulses | Verify reversibility, fatigue resistance | 1–2 weeks |

---

## Success Criteria & Go/No-Go Gates

### Gate 1: Morphology & Adhesion (Month 1)
- ✓ All layers intact, no visible delamination
- ✓ EDS: Elemental distribution uniform (no phase segregation)
- ✓ Adhesion strength: σ_adhesion > 5 MPa

**Go condition**: All three criteria met  
**No-go action**: Optimize sintering, surface prep, or interface layer

### Gate 2: Thermoelectric Response (Month 3)
- ✓ Seebeck coefficient: S > 50 µV/K (detectable signal)
- ✓ Power factor: PF > 0.5 µW/cm-K² (non-trivial)
- ✓ Thermal conductivity: κ < 5 W/m-K (phonon scattering achieved)

**Go condition**: At least 2 of 3 criteria met  
**No-go action**: Adjust composition, twist angle, or doping level

### Gate 3: Magnetic Switching (Month 2.5)
- ✓ Switching probability: P_switch > 30%
- ✓ Switching time: τ < 1 ns
- ✓ No immediate failure after 1000 cycles

**Go condition**: All three criteria met  
**No-go action**: Tune pulse amplitude/width, modify magnetic layer composition

### Gate 4: Healing Kinetics (Month 4)
- ✓ Crack closure: η > 60% within 48 h at T_heal
- ✓ Conductivity recovery: ΔR/R < 50%
- ✓ Repeatable: Healing works for ≥3 cycles

**Go condition**: All three criteria met  
**No-go action**: Increase polymer cross-linking, optimize healing temperature

### Gate 5: Durability (Month 5)
- ✓ Thermal cycling: No delamination after 20 cycles
- ✓ Property retention: <30% drop in κ, σ, S after cycling
- ✓ Salt spray: <5 mm² corrosion area

**Go condition**: All three criteria met  
**No-go action**: Strengthen interfaces, improve protective layer coverage

---

## Specimen Preparation & Documentation

### Sample ID Convention
```
MEAQT-[Stack]–[Substrate]–[Protective]–[Rep#]–[Date]
Example: MEAQT-HEA-SiC-Vitrimer-03-20260715
```

### Mandatory Records
- Synthesis batch number & conditions
- As-measured layer thicknesses (SEM)
- XRD phase ID
- Baseline transport data
- All measurement dates & technician initials

---

## Comparison to Literature Benchmarks

| Property | Literature | MEAQ-T Target | Status |
|----------|-----------|---|---|
| **Seebeck (HEA thermoelectrics)** | 50–150 µV/K | >75 µV/K | Stretch |
| **Thermal conductivity (HEA)** | 1–4 W/m-K | 2–3 W/m-K | Achievable |
| **Hardness (oxide ceramic)** | 1000–2000 HV | 1200–1800 HV | Achievable |
| **Healing efficiency (vitrimer)** | 70–95% | >80% | Achievable |
| **Thermal shock cycles** | 5–30 (typical coatings) | >20 | Stretch |
| **Pulse-switching speed (2D materials)** | 10–100 ps | <500 ps | Achievable |

---

## Resource Allocation & Staffing

| Phase | Personnel | Equipment | Budget (Est.) |
|-------|-----------|-----------|---|
| **Tier 1–2** | 1 PhD/postdoc + 1 technician | On-site lab | $50–80 k |
| **Tier 3–4** | 1 PhD + facility access | PPMS, SQUID, Kerr setup (external) | $100–150 k |
| **Tier 5–6** | 1 PhD + beam facility staff | Ion beam, TEM (external) | $200–300 k |
| **Total** | 2–3 FTE over 12–18 months | Mix of on-site and external | **$400–600 k** |

---

## References & Related Docs

- [Synthesis Protocol](SYNTHESIS_PROTOCOL.md): How to make the samples
- [Risk Assessment](RISK_ASSESSMENT.md): Feasibility gates and contingencies
- [Literature Database](LITERATURE.md): Key experimental benchmarks by pillar
