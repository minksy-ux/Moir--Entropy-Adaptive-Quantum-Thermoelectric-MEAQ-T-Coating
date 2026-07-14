# MEAQ-T Novelty Evidence Map

This document maps external literature to the novelty claims of the MEAQ-T concept.

Scope note:
- Several entries below were provided as rapid literature anchors and should be treated as candidate references until DOI, issue, and pagination metadata are verified.
- The goal is to make novelty framing explicit and actionable for proposals, papers, and milestone reviews.
- BibTeX source for these anchors: [docs/references.bib](references.bib).

## 1) Moire Thermoelectricity and Heavy-Fermion Correlations

Primary anchors:
1. Thermoelectricity of Moire Heavy Fermions in MoTe2/WSe2 Bilayers (Zhang et al., Phys. Rev. Lett. 2026 / arXiv:2510.26958).
2. Moire-pattern-assisted thermoelectric enhancement in twisted WSe2 bilayer (Kumar et al., Phys. Chem. Chem. Phys. 2026).
3. Ultra-Low Thermal Conductivity of Moire Diamanes (related moire phonon-suppression study).
4. Colossal Layer Nernst Effect in Twisted Moire Layers.
5. Emerging Characteristics and Properties of Moire Materials (review article).

Relevance to MEAQ-T novelty:
1. Supports quantitative Seebeck control and sign changes linked to correlation physics (Kondo-coherence and Zeeman-breakdown regimes).
2. Supports entropy accumulation and strongly correlated transport in MoTe2/WSe2 moire phases.
3. Supports lattice thermal-conductivity suppression from moire-modulated phonon scattering, reinforcing low-kappa design assumptions.
4. Supports transverse thermoelectric channels (Nernst-style observables) aligned with the current nernst_proxy objective.
5. Supports broad physical plausibility across flat bands, correlations, and tunable quantum transport.

## 2) High-Entropy Engineering for Thermoelectrics and Coatings

Primary anchors:
1. High-Entropy Engineering in Thermoelectric Materials: A Review.
2. Review of high-entropy thermoelectric materials: design, synthesis, characterization, and properties.
3. High- and medium-entropy nitride coatings in Cr-Hf-Mo-Ta-family systems (harsh-environment coating relevance).
4. Atomic-to-nanoscale chemical fluctuation studies in high-entropy thermoelectrics with ultralow lattice thermal conductivity.

Relevance to MEAQ-T novelty:
1. Supports entropy-driven phase stabilization as a central design lever.
2. Supports multi-principal-element screening strategies consistent with composition.py and coating optimizer objectives.
3. Supports concurrent goals of durability and thermal management in protective/interlayer stacks.
4. Supports the hypothesis that configurational complexity can reduce lattice thermal conductivity while preserving useful electrical transport windows.

## 3) Spin Texture Control and Pulse Switching

Primary anchors:
1. Super-moire spin textures in twisted two-dimensional antiferromagnets.
2. Double-pulse control of all-optical magnetization reversal in Tb/Co multilayers.
3. Thermal generation, manipulation and thermoelectric detection of skyrmions.
4. Related ultrafast laser-driven and all-optical switching reports in 2D/kagome systems.

Relevance to MEAQ-T novelty:
1. Supports moire-enabled topological spin-texture formation and control pathways.
2. Supports pulse-domain switching design assumptions used in pulse_response.py.
3. Supports thermoelectric readout coupling to magnetic texture states.
4. Supports extending macrospin scaffolds toward skyrmion-aware pulse control in later milestones.

## 4) Self-Healing Coatings for Extreme Environments

Primary anchors:
1. Self-Healing Coatings in Extreme Environments (review).
2. Self-healing ceramic coatings: mechanisms, design strategies, and emerging applications for extreme environments.
3. Intelligent self-healing polymeric systems for functional and durable coatings.
4. Extreme-environment-resistant self-healing anti-icing coating examples.
5. Glaze-enabled healing ceramics and HfB2-SiC-TaSi2 systems with high-temperature ablation resistance and in-situ healing.

Relevance to MEAQ-T novelty:
1. Supports the dual-track healing strategy (dynamic-covalent polymeric and oxidation/viscous-flow ceramic pathways).
2. Supports integrating self-healing functionality into harsh-environment coating stacks, not only soft polymers.
3. Supports material-basis selection already reflected in candidate protective layers.
4. Supports the claim that repairability and extreme-environment survivability can be co-optimized.

## 5) Integrated Novelty Claim (Cross-Domain)

The novelty of MEAQ-T is not any single pillar in isolation, but the integrated co-design of:
1. Correlated moire thermoelectric transport.
2. Entropy-engineered phase stability and low-kappa pathways.
3. Pulse-addressable magnetic/spin-texture dynamics.
4. Self-healing durability under extreme conditions.

This evidence map supports the position that each pillar is literature-grounded, while the combined architecture and optimization workflow remain differentiating.

## 6) How to Use This File in Manuscripts and Proposals

1. Use one anchor from each section to justify each objective term in the optimizer and each module in src/meaqt.
2. Explicitly separate validated measurements from hypotheses in milestone tables.
3. Add DOI and full citation metadata before external release.
4. Keep this file updated as benchmarks and model calibration data are added.

## 7) Citation Key Mapping

Use these keys from [docs/references.bib](references.bib) when drafting manuscripts:

1. zhang2026_moire_heavy_fermion_thermoelectricity
2. kumar2026_twisted_wse2_thermoelectric
3. unknown2026_moire_diamane_low_kappa
4. unknown2026_colossal_layer_nernst
5. unknown_review_moire_materials
6. unknown_review_high_entropy_thermoelectric
7. unknown_review_he_thermoelectric_design
8. unknown_cr_hf_mo_ta_nitride_coatings
9. unknown_super_moire_spin_textures
10. unknown_double_pulse_all_optical_reversal
11. unknown_thermal_skyrmion_thermoelectric_detection
12. unknown_review_self_healing_extreme
13. unknown_review_self_healing_ceramic
14. unknown_review_intelligent_polymeric_healing
15. unknown_extreme_anti_icing_healing
