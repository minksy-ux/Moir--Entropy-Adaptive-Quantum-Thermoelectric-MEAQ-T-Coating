# MEAQ-T Coating: Risk Assessment & Feasibility Framework

**Status**: Go/no-go decision gates and confidence scoring  
**Last Updated**: 2026-07-15  
**Decision Authority**: Project steering committee

---

## Executive Summary

This document defines **quantified feasibility gates** at each project milestone. Each gate has:
- **Target metrics** (thermoelectric, magnetic, durability properties)
- **Confidence scoring** (0–100%) for success probability
- **Decision criteria** (go/no-go/conditional)
- **Fallback options** (contingent design changes if gate fails)

---

## Confidence Scoring Methodology

**Scoring Components**:
- **Literature precedent** (0–30 pts): How many published examples exist?
- **Simulation accuracy** (0–20 pts): How well do predictive models match experiments?
- **Manufacturing feasibility** (0–25 pts): Can we reliably produce this layer?
- **Characterization certainty** (0–15 pts): How definitive are our measurements?
- **Technology maturity** (0–10 pts): TRL (Technology Readiness Level) assessment

**Scoring Ranges**:
- **90–100%**: Excellent precedent, proven manufacturing, high confidence
- **70–89%**: Good precedent, moderate manufacturing challenges, acceptable risk
- **50–69%**: Limited precedent, significant challenges, high-risk development
- **20–49%**: Minimal precedent, major technical challenges, very high risk
- **<20%**: Speculative, not recommended without major research investment

---

## Gate 1: Substrate Preparation & Interface Engineering

**Timeline**: Month 1  
**Objective**: Establish reproducible substrate cleaning and interface layer

### Acceptance Criteria

| Metric | Target | Confidence |
|--------|--------|---|
| **Surface cleanliness** (visual + SEM) | No visible particles, clean SiO₂ interface | 95% |
| **Contact angle** | <30° (hydrophilic) | 95% |
| **Interface layer adhesion** | >5 MPa (pull-off test) | 85% |
| **Reproducibility** (3 samples) | CV of adhesion <15% | 80% |

### Confidence Assessment

| Component | Score | Justification |
|-----------|-------|---|
| **Literature precedent** | 28/30 | Extensive prior art in ceramic coating adhesion; standard protocols (ASTM) exist |
| **Simulation accuracy** | 18/20 | Surface energy calculations well-established; minimal uncertainty |
| **Manufacturing feasibility** | 23/25 | Grit blasting & chemical cleaning standard industry practice |
| **Characterization certainty** | 14/15 | Pull-off testing well-standardized; minor equipment variation |
| **Technology maturity** | 9/10 | TRL 8–9 (proven in production) |
| **TOTAL CONFIDENCE** | **92/100** | **GO with high confidence** |

### Decision Logic

```
IF (adhesion > 5 MPa AND CV < 15% AND contact angle < 30°) THEN
  STATUS = GO (proceed to Gate 2)
ELSE IF (adhesion > 3 MPa AND CV < 25%) THEN
  STATUS = CONDITIONAL (iterate substrate prep, re-test)
ELSE
  STATUS = NO-GO (fallback: use alternative adhesion promoter)
```

### Fallback Options (if NO-GO)

1. **Silane coupling agent**: Apply γ-methacryloxypropyltrimethoxysilane (MPTS) to substrate
2. **Plasma activation**: 5 min O₂ plasma surface treatment
3. **Rougher grit**: Upgrade to 80-mesh grit blasting (more aggressive surface)
4. **Extended interface layer**: Thicken compliance layer from 10 µm → 30 µm

---

## Gate 2: High-Entropy Interlayer Phase Stability

**Timeline**: Month 2  
**Objective**: Produce single-phase (or near-single-phase) HEA without unwanted decomposition

### Acceptance Criteria

| Metric | Target | Confidence |
|--------|--------|---|
| **Phase purity** (XRD) | >90% primary phase (allow <10% secondary) | 80% |
| **Elemental distribution** (EDS) | Uniform across layer, no segregation >2× | 85% |
| **Thermal stability** | No phase change after 1000 h @ 1000°C | 70% |
| **Hardness** | 1200–1800 HV (single-phase expected) | 80% |

### Confidence Assessment

| Component | Score | Justification |
|-----------|-------|---|
| **Literature precedent** | 20/30 | HEAs are ~15-year-old field; equiatomic oxides less common than alloys |
| **Simulation accuracy** | 15/20 | CALPHAD models improve yearly but still have uncertainties in entropy calculations |
| **Manufacturing feasibility** | 18/25 | Sintering control is challenging; minor parameter changes cause phase separation |
| **Characterization certainty** | 13/15 | XRD analysis standard; phase ID can be ambiguous if peak overlap |
| **Technology maturity** | 6/10 | TRL 4–5 (lab prototype stage, not yet proven in production) |
| **TOTAL CONFIDENCE** | **72/100** | **GO with moderate confidence, contingency planning required** |

### Decision Logic

```
IF (phase_purity > 90% AND EDS_uniformity_ratio < 2 AND stability_confirmed) THEN
  STATUS = GO (proceed to Gate 3)
ELSE IF (phase_purity > 75% AND isolated_secondary_phases_benign) THEN
  STATUS = CONDITIONAL (characterize secondary phase, proceed with caution)
ELSE
  STATUS = NO-GO (fallback: reformulate composition or adjust sintering)
```

### Fallback Options (if NO-GO)

1. **Composition adjustment**: Increase number of elements (4 → 5 or 6) to boost entropy
2. **Lower sintering temperature**: 1400°C → 1250°C (reduces diffusion-driven ordering)
3. **Shorter dwell time**: 2 h → 30 min at peak (quench-lock high-entropy state)
4. **Material substitution**: Replace equiatomic with slightly off-stoichiometric composition targeting known stable ternaries as stabilizers

---

## Gate 3: Moire Layer 2D Material Quality & Transfer

**Timeline**: Month 2.5  
**Objective**: Successfully stack MoTe₂/WSe₂ with acceptable twist angle and interface quality

### Acceptance Criteria

| Metric | Target | Confidence |
|--------|--------|---|
| **Twist angle precision** | 1.1° ± 0.2° (Bragg alignment confirmed) | 60% |
| **Raman linewidth** (monolayer A₁g) | FWHM < 4 cm⁻¹ (quality indicator) | 70% |
| **Layer continuity** | >80% coverage (SEM inspection) | 75% |
| **Interfacial adhesion** | No visible bubbles/wrinkles in optical microscopy | 80% |

### Confidence Assessment

| Component | Score | Justification |
|-----------|-------|---|
| **Literature precedent** | 18/30 | 2D stacking is 8-year field; moire devices ~5 years old; published examples exist but not routine |
| **Simulation accuracy** | 12/20 | Band structure models are good; but twist angle control uncertainty remains |
| **Manufacturing feasibility** | 15/25 | Mechanical transfer via TRT is labor-intensive, low-yield prototype method; not yet scalable |
| **Characterization certainty** | 12/15 | Raman & AFM reliable; but optical alignment judgment subjective |
| **Technology maturity** | 4/10 | TRL 2–3 (research prototype, single samples, high failure rate) |
| **TOTAL CONFIDENCE** | **61/100** | **GO with conditional acceptance; expect significant iteration** |

### Decision Logic

```
IF (twist_angle_within_0.2° AND FWHM < 4 AND coverage > 80%) THEN
  STATUS = GO (proceed to Gate 4)
ELSE IF (coverage > 60% AND FWHM < 5 AND twist_rough_estimate_OK) THEN
  STATUS = CONDITIONAL (accept sample for characterization, recognize limitations)
ELSE
  STATUS = NO-GO (fallback: source pre-made heterostructure from vendor, or re-attempt transfer)
```

### Fallback Options (if NO-GO)

1. **Vendor-sourced 2D stack**: Buy pre-stacked MoTe₂/WSe₂ from graphene company (cost increase ~$500–2000, long lead time)
2. **Simpler 2D system**: Use monolayer MoS₂ (simpler, more robust, but potentially lower Seebeck)
3. **CVD growth**: Grow MoTe₂ and WSe₂ in-house or via fab (longer timeline, requires reactor setup)
4. **Abandon 2D layer**: Test HEA/protective stack alone to decouple HEA performance; add 2D layer in Phase 2

---

## Gate 4: Thermoelectric Transport Proof-of-Concept

**Timeline**: Month 3  
**Objective**: Demonstrate measurable Seebeck coefficient and non-trivial power factor

### Acceptance Criteria

| Metric | Target | Confidence |
|--------|--------|---|
| **Seebeck coefficient** | S > 50 µV/K (detectable) | 75% |
| **Power factor** | PF > 0.5 µW/cm-K² | 65% |
| **Thermal conductivity** | κ < 5 W/m-K (confirmed low) | 85% |
| **Figure of merit** | ZT > 0.05 (>0 is success) | 60% |

### Confidence Assessment

| Component | Score | Justification |
|-----------|-------|---|
| **Literature precedent** | 22/30 | HEA thermoelectrics: 10-year field with numerous papers; moire enhancement speculative but plausible |
| **Simulation accuracy** | 14/20 | Boltzmann transport models validated; but moire band structure details uncertain |
| **Manufacturing feasibility** | 16/25 | Transport measurement well-established; but coating uniformity may degrade transport |
| **Characterization certainty** | 13/15 | ZEM and PPMS are standard; but small-sample effects can cause uncertainty |
| **Technology maturity** | 7/10 | TRL 5–6 (bench demonstration of concept) |
| **TOTAL CONFIDENCE** | **72/100** | **GO with moderate confidence; proof-of-concept stage** |

### Decision Logic

```
IF (S > 50 AND PF > 0.5 AND κ < 5 AND ZT > 0.05) THEN
  STATUS = GO (advance to optimization phase)
ELSE IF (S > 20 AND κ < 6 AND ZT detectable) THEN
  STATUS = CONDITIONAL (continue but revise composition/doping targets)
ELSE
  STATUS = NO-GO (fallback: re-evaluate moire benefit vs. baseline HEA alone)
```

### Fallback Options (if NO-GO)

1. **Doping optimization**: Apply gate voltage sweep to find optimal carrier concentration
2. **Twist angle scan**: Produce samples at 0.8° – 1.4° in 0.1° increments
3. **Composition tuning**: Adjust HEA stoichiometry (move away from equiatomic)
4. **Baseline comparison**: Measure HEA-only (no 2D) to quantify moire contribution
5. **Literature review**: If moire doesn't help, focus on HEA alone (lower-risk path)

---

## Gate 5: Magnetic Switching Feasibility

**Timeline**: Month 2.5  
**Objective**: Demonstrate pulse-induced reversible magnetization switching with >30% probability

### Acceptance Criteria

| Metric | Target | Confidence |
|--------|--------|---|
| **Switching probability** | P_switch > 30% | 50% |
| **Switching time** | τ_switch < 1 ns | 55% |
| **State stability** | Remnant magnetization stable >1 h | 65% |
| **Coercivity** (remanent) | H_c > 100 Oe | 70% |

### Confidence Assessment

| Component | Score | Justification |
|-----------|-------|---|
| **Literature precedent** | 12/30 | Pulse-driven switching well-known in magnetic materials, but moire-integrated switching is novel, <5 published examples |
| **Simulation accuracy** | 10/20 | LLG dynamics simulations exist but micromagnetic details complex; topological effects speculative |
| **Manufacturing feasibility** | 12/25 | Interfacial magnetism control is subtle art; high failure rate in development |
| **Characterization certainty** | 11/15 | Kerr microscopy standard; but temporal resolution and noise floor challenging for fast switching |
| **Technology maturity** | 3/10 | TRL 2–3 (research prototype, proof-of-principle only) |
| **TOTAL CONFIDENCE** | **48/100** | **CONDITIONAL / HIGH-RISK – Proceed with significant R&D reserve** |

### Decision Logic

```
IF (P_switch > 30% AND τ < 1ns AND H_c > 100) THEN
  STATUS = GO (advance to optimization phase)
ELSE IF (P_switch > 10% AND τ detectable AND bistability_confirmed) THEN
  STATUS = CONDITIONAL (continue as research objective, lower priority for prototype 1)
ELSE
  STATUS = NO-GO (fallback: defer magnetic switching to Phase 2, focus on thermal/thermoelectric)
```

### Fallback Options (if NO-GO)

1. **Interface engineering**: Optimize Fe/TiO₂ thickness for stronger perpendicular anisotropy
2. **Bias field**: Integrate permanent magnet or electromagnet for H_bias stabilization
3. **Material swap**: Use intrinsic ferromagnet (CrI₃, Cr₂Ge₂Te₆) instead of interfacial magnetism
4. **Pulse parameter tuning**: Systematic sweep of amplitude, duration, polarization
5. **Defer feature**: Keep as stretch goal for later prototype; focus on thermoelectric success first

---

## Gate 6: Self-Healing Kinetics Demonstration

**Timeline**: Month 5  
**Objective**: Prove crack closure with >60% efficiency in first cycle

### Acceptance Criteria

| Metric | Target | Confidence |
|--------|--------|---|
| **Crack closure ratio** | η_heal = (w_init - w_final) / w_init > 60% | 75% |
| **Time to closure** | 24–72 h at T_heal = 100–120°C | 80% |
| **Property recovery** | ΔR/R_initial < 50% (electrical healing) | 70% |
| **Repeated healing** | >80% closure for cycles 2–3 (retain function 3×) | 60% |

### Confidence Assessment

| Component | Score | Justification |
|-----------|-------|---|
| **Literature precedent** | 25/30 | Self-healing polymers extensively studied; vitrimers proven to recover >80% properties |
| **Simulation accuracy** | 16/20 | Healing kinetics models exist but depend on formulation details; prediction ±20% |
| **Manufacturing feasibility** | 21/25 | Vitrimer synthesis well-established; coating deposition routine |
| **Characterization certainty** | 14/15 | Optical microscopy & electrical measurement standard; minimal uncertainty |
| **Technology maturity** | 8/10 | TRL 6–7 (demonstration in relevant environment, some production examples) |
| **TOTAL CONFIDENCE** | **84/100** | **GO with high confidence** |

### Decision Logic

```
IF (η_heal > 60% AND recovery_time < 72h AND ΔR/R < 50% AND cycle_2_success) THEN
  STATUS = GO (advance to durability testing, consider larger-scale prototypes)
ELSE IF (η_heal > 40% AND recovery_possible_with_higher_T) THEN
  STATUS = CONDITIONAL (accept with operational constraint: T_heal > 120°C)
ELSE
  STATUS = NO-GO (fallback: switch to non-self-healing protective layer, or explore PDMS vitrimers)
```

### Fallback Options (if NO-GO)

1. **Temperature increase**: Heal at 130–150°C (accelerates dynamics, accepts higher thermal stress)
2. **Polymer formulation**: Test PDMS or other vitrimer variants for higher healing cycles
3. **Microcapsule addition**: Embed liquid healing agent to supplement polymer flow
4. **Non-healing layer**: Use static protective ceramic (sacrifices self-healing for assured durability)
5. **Hybrid approach**: Healing layer for non-critical areas, ceramic for high-stress regions

---

## Gate 7: Thermal Cycling Endurance (≥20 cycles)

**Timeline**: Month 6  
**Objective**: Survive 20 rapid thermal cycles (room temp ↔ 1000°C) with <30% property degradation

### Acceptance Criteria

| Metric | Target | Confidence |
|--------|--------|---|
| **No delamination** | Zero delamination observed post-cycling | 75% |
| **Property retention** | κ, σ, S maintain >70% of initial values | 70% |
| **Adhesion post-cycling** | >5 MPa (no drop >50%) | 70% |
| **Surface integrity** | <5% area with visible cracks | 75% |

### Confidence Assessment

| Component | Score | Justification |
|-----------|-------|---|
| **Literature precedent** | 20/30 | Thermal cycling of coatings well-studied; but MEAQ-T multi-layer stack novel |
| **Simulation accuracy** | 13/20 | FEA thermal stress models good; but interface failure is complex (depends on exact adhesion quality) |
| **Manufacturing feasibility** | 17/25 | Coating production established; but multi-layer coordination challenging |
| **Characterization certainty** | 12/15 | Thermal cycling rig standard; post-failure analysis well-defined but labor-intensive |
| **Technology maturity** | 6/10 | TRL 5–6 (bench demonstration) |
| **TOTAL CONFIDENCE** | **68/100** | **GO with moderate-high confidence; expect some iterative design** |

### Decision Logic

```
IF (no_delamination AND property_retention > 70% AND adhesion_maintained) THEN
  STATUS = GO (advance to scale-up phase, approve for field trials)
ELSE IF (delamination_at_edge_only AND core_intact AND property_drop < 40%) THEN
  STATUS = CONDITIONAL (accept with operational limit: max 15 cycles before replacement)
ELSE
  STATUS = NO-GO (fallback: strengthen interfaces, add compliance layer, reduce cycle rate)
```

### Fallback Options (if NO-GO)

1. **Interface strengthening**: Add adhesion promoters, increase bonding sintering temperature
2. **Compliance layer**: Thicken gradient interlayer (10 µm → 30 µm)
3. **Slower thermal ramps**: Design for ≤1°C/min (vs. current 5°C/min) to reduce thermal shock
4. **Reduced duty cycle**: Qualify for 10 cycles instead of 20
5. **Material upgrade**: Replace ceramic protective layer with compliant elastomer (lower stress but temperature limit)

---

## Gate 8: Corrosion Resistance (500 h Salt Spray)

**Timeline**: Month 6  
**Objective**: Resist aggressive corrosion environment without substrate exposure

### Acceptance Criteria

| Metric | Target | Confidence |
|--------|--------|---|
| **Corrosion area** | <1% of sample surface | 80% |
| **Pit depth** | <10 µm (SEM inspection) | 75% |
| **Substrate protection** | No substrate visible through corrosion | 85% |
| **Coating integrity** | No delamination or spalling | 80% |

### Confidence Assessment

| Component | Score | Justification |
|-----------|-------|---|
| **Literature precedent** | 24/30 | Ceramic coating corrosion resistance well-documented; specific stack untested |
| **Simulation accuracy** | 14/20 | Electrochemical models exist but porosity effects uncertain |
| **Manufacturing feasibility** | 20/25 | Standard coating process; minor defects affect corrosion performance |
| **Characterization certainty** | 14/15 | Salt spray testing standardized (ASTM B117) |
| **Technology maturity** | 8/10 | TRL 6–7 (proven in deployment) |
| **TOTAL CONFIDENCE** | **80/100** | **GO with high confidence** |

### Decision Logic

```
IF (corrosion_area < 1% AND pit_depth < 10µm AND substrate_protected) THEN
  STATUS = GO (qualify for marine/automotive environments)
ELSE IF (corrosion_area < 5% AND substrate_still_protected) THEN
  STATUS = CONDITIONAL (accept for limited deployment, 1–2 years max)
ELSE
  STATUS = NO-GO (fallback: seal edges, add hydrophobic topcoat, increase protective layer thickness)
```

### Fallback Options (if NO-GO)

1. **Edge sealing**: Apply epoxy or silicone sealant around perimeter
2. **Hydrophobic topcoat**: 5 µm wax or silicone layer on surface
3. **Thicker protective layer**: 100 µm → 200 µm (longer diffusion path)
4. **Material upgrade**: Replace vitrimer with hermetic ceramic topcoat (no water permeation)
5. **Cathodic protection**: Integrate sacrificial Zn or Mg insert at edges

---

## Gate 9: Radiation Hardness (Advanced, Optional Phase 2)

**Timeline**: Month 10 (optional, depends on mission profile)  
**Objective**: Maintain >80% of transport properties after 10¹⁸ cm⁻² irradiation fluence

### Acceptance Criteria

| Metric | Target | Confidence |
|--------|--------|---|
| **Property retention** (κ, σ, S) | >80% post-irradiation | 50% |
| **Defect annealing** | Recovery possible via 1000°C anneal, 1 h | 60% |
| **No amorphization** | Raman/XRD confirm crystallinity retained | 55% |

### Confidence Assessment

| Component | Score | Justification |
|-----------|-------|---|
| **Literature precedent** | 15/30 | Radiation damage of HEAs limited; moire 2D materials even less studied |
| **Simulation accuracy** | 8/20 | SRIM estimates good; but defect clustering & cascade details uncertain |
| **Manufacturing feasibility** | 10/25 | Irradiation facilities specialized; limited access |
| **Characterization certainty** | 10/15 | Transport measurement post-irradiation standard; but small effects hard to discern |
| **Technology maturity** | 2/10 | TRL 1–2 (early research concept) |
| **TOTAL CONFIDENCE** | **45/100** | **CONDITIONAL / HIGH-RISK – Major research needed** |

### Decision Logic

```
IF (property_retention > 80% AND no_amorphization) THEN
  STATUS = GO (qualify for space/nuclear environments)
ELSE IF (property_drop 20-40% AND recovery_via_annealing_acceptable) THEN
  STATUS = CONDITIONAL (accept with maintenance protocol: periodic annealing)
ELSE
  STATUS = NO-GO (fallback: accept limited radiation duty, or research alternative materials)
```

### Fallback Options (if NO-GO)

1. **Material substitution**: Switch to known radiation-hard ceramics (SiC, Al₂O₃)
2. **Shielding**: Add boron or cadmium layer to reduce flux to sensitive layers
3. **Annealing protocol**: Accept periodic 1000°C anneals to recover defects
4. **Duty limitation**: Qualify only for <10¹⁷ cm⁻² (lower radiation environments)
5. **Defer feature**: Keep as stretch goal; focus on terrestrial thermal/thermoelectric applications

---

## Summary: Master Go/No-Go Decision Tree

```
PROJECT SUCCESS CRITERIA:

PHASE 1 COMPLETION (Month 6):
├─ Gate 1 (Substrate prep): GO
├─ Gate 2 (HEA phase): GO or CONDITIONAL (→ optimization loop)
├─ Gate 3 (2D moire): GO or CONDITIONAL (→ vendor fallback)
├─ Gate 4 (Transport): GO or CONDITIONAL (→ parameter scan)
├─ Gate 5 (Magnetic switch): CONDITIONAL (→ defer if needed, not critical for Prototype 1)
├─ Gate 6 (Self-healing): GO or CONDITIONAL (→ temperature optimization)
└─ Gates 7–8 (Durability): GO or CONDITIONAL (→ interface strengthening)

PROTOTYPE 1 READY: All Gates 1–4, 6–8 at GO or CONDITIONAL with clear mitigation
RISK LEVEL: Moderate (expect 20–30% design iteration if any gates conditional)

PHASE 2 COMPLETION (Month 12):
├─ All Phase 1 gates advanced to stable GO
├─ Scale-up process window defined (>5 successful batches, CV <20%)
├─ Field demonstration trial initiated
└─ Gate 9 (Radiation): Optional, pursue if mission requires

PRODUCTION READINESS: All gates stable GO, process controls in place, cost <$XX/m²
```

---

## Resource Planning & Budget Allocation

| Phase | Timeline | Budget | Staff | Key Risks |
|-------|----------|--------|-------|---|
| **Phase 1** (Gates 1–8) | Months 1–6 | $200–300 k | 2–3 FTE (PhD + technician) | Gates 3, 5 (novel tech) |
| **Phase 2** (Scale-up) | Months 7–12 | $300–400 k | 2 FTE + fab specialist | Process reproducibility |
| **Phase 3** (Production) | Year 2+ | $500+ k/yr | 5+ FTE | Yield, cost control |
| **TOTAL (Year 1)** | 12 months | **$500–700 k** | **4–5 FTE** | **Tech readiness + manufacturing** |

---

## References & Related Documents

- [FMEA](FMEA.md): Detailed failure analysis linked to gates
- [Characterization Plan](CHARACTERIZATION_PLAN.md): How to measure success at each gate
- [Synthesis Protocol](SYNTHESIS_PROTOCOL.md): Manufacturing procedures
- [Collaboration Map](COLLABORATION_MAP.md): Required expertise & facilities
