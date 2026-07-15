# MEAQ-T Coating Synthesis Protocol

**Status**: Preliminary scaffold for laboratory translation  
**Level**: Research prototype (non-optimized)  
**Last Updated**: 2026-07-15

---

## Overview

MEAQ-T coating assembly follows a **bottom-up, layer-by-layer** approach targeting extreme-environment protection with adaptive thermal and magnetic response. This document provides actionable procedures for each layer stack component.

### Baseline Stack Architecture

```
┌─────────────────────────────────────────┐
│ 1. Top Protective Layer                 │ ← UV/curing or sinter
│    (Bio-vitrimer or UHTC ceramic)       │
├─────────────────────────────────────────┤
│ 2. High-Entropy Interlayer              │ ← Solid-state or slurry
│    (Oxide, carbide, or perovskite HEA)  │
├─────────────────────────────────────────┤
│ 3. Moire Active Layer                   │ ← Dry transfer or CVD
│    (2D heterostructures in hBN)         │
├─────────────────────────────────────────┤
│ 4. Compliance Layer                     │ ← Graded composition
│    (Gradient interlayer for adhesion)   │
├─────────────────────────────────────────┤
│ 5. Substrate                            │ ← Prepared interface
│    (SiC or ceramic composite)           │
└─────────────────────────────────────────┘
```

---

## Layer 1: Substrate Preparation & Interface Engineering

### 1.1 Substrate Selection & Cleaning

**Materials**: SiC composite, Al₂O₃, or steel (depending on service temperature)

**Procedure**:
1. **Mechanical cleaning**
   - Grit blast with 120–220 mesh Al₂O₃ powder
   - Flow rate: 0.5–1.0 kg/min, pressure: 60–80 psi
   - Distance: 100–150 mm, angle: 30–45°
   - Duration: Until surface uniformly matted (typically 2–3 min)

2. **Chemical cleaning**
   - Immerse in acetone (ACS grade) for 5 min
   - Sonicate at 40 kHz for 3 min
   - Repeat with ethanol (200 proof)
   - Air dry at room temperature or 60°C for 5 min

3. **Surface verification**
   - Contact angle: <30° (hydrophilic)
   - SEM inspection: No residual debris or oxidation

### 1.2 Graded Interface Layer (Optional but Recommended)

**Purpose**: Mitigate thermal mismatch and improve adhesion

**Material**: SiC or Al₂O₃ nanoparticles in epoxy or silicate binder

**Procedure**:
1. Mix nanoparticles (5–10 wt%) with binder
2. Coat onto substrate (spin coat, 3000 rpm, 30 s)
3. Cure per binder specification (typically 80°C, 2 h)
4. Density: Target ≥95% by ultrasonic measurement

---

## Layer 2: High-Entropy Interlayer Deposition

### 2.1 Oxide HEA Route: (Hf, Zr, Ta, Nb, Ti)O

**Preferred for**: Thermal stability, phase robustness

**Starting Materials**:
- Metal chlorides or nitrates (99.99% purity)
- Molar composition: Equiatomic (20% each element)

#### Option A: Solid-State Sintering (Low-cost, Lab-friendly)

1. **Precursor synthesis**
   - Mix oxides (HfO₂, ZrO₂, Ta₂O₅, Nb₂O₅, TiO₂) in 1:1:1:1:1 molar ratio
   - Mill in zirconia jar, 500 rpm, 4 h
   - Sieve <100 mesh

2. **Consolidation**
   - Press powder in tungsten die to 80% theoretical density
   - Cold isostatic press (CIP): 100 MPa, room temperature, 1 min
   - Measure green density (Archimedes method with CCl₄)

3. **Sintering profile**
   - Ramp: 2°C/min to 1400°C (inert Ar atmosphere)
   - Dwell: 1400°C, 2 h
   - Cool: Furnace cool to <200°C
   - Final density target: ≥90% TD (theoretical density)

4. **Coating onto substrate**
   - Grind sintered HEA to powder (<5 µm)
   - Slurry: 70 wt% HEA powder + 30 wt% silicate binder
   - Spray coat or dip coat onto substrate
   - Dry: 80°C, 2 h; **Sinter again**: 1200°C, 1 h (bonding)

**Thickness target**: 50–100 µm

#### Option B: Pechini Method (Higher purity, sol-gel)

1. **Solution preparation**
   - Dissolve metal nitrates in DI water (1 M each)
   - Add citric acid (1:1 molar ratio to metals)
   - Stir at 60°C for 30 min
   - Add ethylene glycol (same volume as water)
   - Heat to 120°C for 4 h (polyesterification)

2. **Gel-to-powder conversion**
   - Dry at 120°C overnight → gel
   - Pre-calcine at 400°C, 2 h (ramp 1°C/min)
   - Calcine at 800°C, 2 h → powder

3. **Consolidation on substrate**
   - Disperse powder in isopropanol (100 mg/mL)
   - Dip coat substrate (5–10 passes, dry between each)
   - Final sinter: 1200°C, 2 h in Ar

**Thickness target**: 30–80 µm

### 2.2 Interlayer Characterization

**Critical measurements**:
- **XRD**: Confirm single-phase or limited second phases
- **SEM/EDS**: Elemental distribution, porosity <10%
- **Thermal conductivity**: κ ≈ 1–2 W/m-K (measure by laser flash)
- **Adhesion**: Scratch test or tensile pull (>10 MPa bonding strength)

---

## Layer 3: Compliance/Adhesion Layer

### 3.1 Graded Composition Gradient

**Purpose**: Buffer thermal expansion mismatch between HEA and moire layer

**Procedure**:
1. Create 3-layer gradient:
   - Bottom 10 µm: 100% HEA composition
   - Middle 10 µm: 50% HEA + 50% of moire-layer material
   - Top 10 µm: 100% moire-layer material

2. Apply via **multi-step sintering** or **CVD** of intermediate compositions

---

## Layer 4: Moire Active Layer (2D Heterostructures)

### 4.1 CVD or Dry Transfer of 2D Materials

**Materials**: MoTe₂/WSe₂ heterostructure encapsulated in hBN

**Option A: Mechanical Dry Transfer (Reproducible for prototypes)**

**Equipment needed**:
- Thermal release tape (TRT) system
- Microscope with XY stage
- Temperature controller (80–120°C)
- Optical alignment

**Procedure**:
1. **Prepare h-BN substrate**
   - Source: Graphene Council suppliers, >99.9% purity
   - Flake size: 50–200 nm thick, prepare on SiO₂
   - Clean: 300°C in air, 30 min (remove contamination)

2. **Acquire MoTe₂ monolayer**
   - Obtain from CVD growth (external fab or in-house CVD reactor)
   - Or mechanical exfoliation from bulk crystal
   - Target: Few-layer flakes (1–3 layers)

3. **Stack MoTe₂ on hBN (bottom)**
   - Place MoTe₂ flake on thermal release tape
   - Align over hBN substrate with microscope
   - Lower onto hBN at room temperature
   - Release tape by heating to 100°C, peel slowly

4. **Transfer WSe₂ on top**
   - Repeat process with WSe₂ flake (10–30° twist angle for moire)
   - Use **rotation stage** for twist angle control

5. **Encapsulate in hBN**
   - Place top hBN flake on tape
   - Align and transfer onto stack
   - Anneal at 250°C in vacuum for 30 min (improve contact)

**Thickness**: Typically 1–10 nm (mono- to few-layer)

**Quality checks**:
- Optical microscopy: No wrinkles or tears
- Raman spectroscopy: Sharp A₁g, E'(TO) peaks
- Atomic force microscopy (AFM): Surface roughness <1 nm

### 4.2 Encapsulation & Protection

**Purpose**: Prevent oxidation and mechanical damage

**Procedure**:
1. Deposit 10–50 nm SiO₂ by atomic layer deposition (ALD) or thermal oxidation
2. Or apply **polymer topcoat** (see Layer 1 below)

---

## Layer 1: Top Protective Layer (Now Applied Last)

### 5.1 Bio-Vitrimer Route (Moderate Temperature)

**Use case**: T < 150°C, requires healing capability

**Materials**:
- Methacrylated vanillin (MV): 40 wt%
- Flexible diamine (e.g., DMAP): 30 wt%
- Methacrylated eugenol (ME): 20 wt%
- Functionalized SiO₂ nanoparticles (2 wt%)
- Photoinitiator (Irgacure 651): 1 wt%

**Procedure**:
1. **Synthesis**
   - Mix MV, ME in solvent (CHCl₃) at 60°C
   - Add SiO₂ nanoparticles, sonicate 10 min
   - Add diamine solution slowly
   - Stir at room temperature for 1 h

2. **Coating application**
   - Spin coat: 2000 rpm, 30 s
   - Or dip coat: 5 cm/min withdrawal rate
   - Layer thickness: 10–50 µm

3. **Photocuring**
   - UV exposure (365 nm): 100–200 mW/cm², 5–10 min
   - Temperature: 20–25°C (or 50°C for accelerated cure)

4. **Post-cure thermal treatment**
   - Heat to 100°C, hold 2 h (vitrification)
   - Cool to room temperature

**Expected properties**:
- Hardness: Shore D ≈ 70–75
- Healing temperature window: 80–120°C
- Crack closure: >80% within 24 h at 100°C

### 5.2 Ultra-High-Temperature Ceramic Route (Extreme Conditions)

**Use case**: T > 1500°C, extreme radiation/thermal shock

**Materials**:
- HfB₂ or ZrB₂ powder (99.9%, <1 µm)
- SiC whiskers (5–10 wt%)
- Silicate binder (water-based or sol-gel)

**Procedure**:
1. **Slurry preparation**
   - Mix HfB₂ powder with SiC whiskers
   - Add water and silicate binder (10 wt%)
   - Ball mill: 24 h, zirconia media

2. **Coating**
   - Spray coat in passes (drying between each)
   - Target thickness: 100–300 µm
   - Each coat: 50 µm target

3. **Sintering consolidation**
   - Dry: 80°C, 4 h
   - Pre-sinter: 400°C, 2 h
   - High-temp sinter: 1600°C, 1 h (inert atmosphere)
   - Cool: Furnace cool

**Expected properties**:
- Melting point: >3000°C
- Thermal conductivity: 20–60 W/m-K
- Radiation resistance: Suitable for high-flux environments

---

## Quality Control & Testing Schedule

### Checkpoint 1: After Substrate Prep
- [ ] Visual inspection (no scratches, clean)
- [ ] Contact angle measurement
- [ ] SEM of surface

### Checkpoint 2: After HEA Interlayer
- [ ] XRD phase analysis
- [ ] SEM cross-section, porosity estimate
- [ ] Thermal conductivity (laser flash, if available)
- [ ] Adhesion test (scratch or pull)

### Checkpoint 3: After Moire Stack
- [ ] Optical microscopy (alignment, wrinkles)
- [ ] Raman spectroscopy (peak positions, linewidths)
- [ ] AFM surface roughness

### Checkpoint 4: After Protective Layer
- [ ] Thickness measurement (caliper, ellipsometry, or SEM)
- [ ] Hardness (Vickers or Shore)
- [ ] Thermal shock resistance (rapid heating/cooling cycle)
- [ ] Electrical conductivity mapping (if relevant)

---

## Troubleshooting Guide

| Issue | Likely Cause | Mitigation |
|-------|--------------|-----------|
| **Poor HEA densification** | Low sintering temp or short dwell | Increase to 1400–1500°C, extend to 3 h |
| **Moire layer delamination** | Weak interface, contamination | Improve surface prep, use adhesion promoter |
| **Protective layer cracking** | Thermal mismatch or shrinkage | Use graded interface, reduce heating rate |
| **Oxidation of 2D materials** | Incomplete encapsulation | Verify SiO₂ coverage, increase thickness |
| **Healing failure** | Insufficient polymer cross-linking | Increase UV dose or cure temperature |

---

## Safety Considerations

- **HfB₂ dust**: Inhalation hazard → use fume hood, wear P100 mask
- **UV curing**: Eye protection required (UV goggles, long sleeves)
- **High-temperature sintering**: Do not open furnace until <200°C
- **Chlorinated solvents** (if used in CVD precursors): Use only with adequate ventilation
- **Thermal shock**: Allow slow cooling to avoid cracking and injury risk

---

## Material Sourcing

### Recommended Suppliers

| Material | Supplier | Grade | Cost (approx.) |
|----------|----------|-------|---|
| HfO₂, ZrO₂ powder | Sigma-Aldrich, Alfa Aesar | 99.9% | $50–200/kg |
| Pechini precursors | Sigma-Aldrich | 99%+ | $100–300/mol equiv |
| hBN flakes | Graphene Council, graphene.info | >99.9% | $500–2000/g |
| MoTe₂ monolayer | External CVD growth or mechanical | Research grade | $200–1000/sample |
| Silicate binder | ColloMil, Zeon | Water-based | $50–150/L |
| HfB₂ UHTC powder | Materion, Advanced Materials | 99.9%, <1 µm | $500–2000/kg |

---

## Timeline Estimate (Full Stack)

| Step | Duration | Notes |
|------|----------|-------|
| Substrate prep | 1 day | Includes cleaning & interface layer |
| HEA sintering | 3–5 days | (Includes drying, pre-sinter, main sinter) |
| 2D transfer stack | 2–3 days | Requires practice & skill; multiple attempts expected |
| Protective layer + cure | 1–2 days | Depends on coating thickness & UV availability |
| **Total (prototype)** | **7–12 days** | Parallelization reduces wall-clock time |

---

## Next Steps & Optimization

1. **Calibration runs**: Produce 5–10 samples with varying parameters (temp, dwell, thickness) to establish process windows
2. **Reproducibility study**: Repeat "golden" sample 3 times, measure variation
3. **Failure analysis**: Intentionally overheat or thermally shock 1–2 samples to identify weak points
4. **Scale-up pathway**: Transition from lab coating to batch production (larger area, automated spray)

---

## References & Related Documents

- MEAQ-T README: Overview of design rationale
- [Characterization Plan](CHARACTERIZATION_PLAN.md): What to measure after synthesis
- [Risk Assessment](RISK_ASSESSMENT.md): Feasibility gates & mitigation
- [Literature Database](LITERATURE.md): Key papers on HEAs, 2D materials, and healing coatings
