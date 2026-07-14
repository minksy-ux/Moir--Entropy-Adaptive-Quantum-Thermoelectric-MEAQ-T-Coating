# MEAQ-T Coating

Moir-Entropy-Adaptive Quantum-Thermoelectric (MEAQ-T) Coating is a proposed class of adaptive functional coatings that unifies:

1. Moire-engineered quantum transport
2. Entropy-driven phase stability
3. Ultrafast pulse-switchable magnetization
4. Autonomous self-healing under extreme environments

The project goal is to move beyond isolated effects and toward one reconfigurable coating platform that can sense, harvest, adapt, and recover in real time.

## Vision

The long-term objective is an engineered coating that can:

1. Harvest thermal gradients via quantum-enhanced thermoelectric transport.
2. Dynamically reconfigure electronic and magnetic states under optical or thermal pulses.
3. Maintain structural and functional integrity in harsh conditions:
	- High radiation flux
	- Thermal shock and steep temperature cycling
	- Chemically aggressive environments
4. Self-heal defects and microcracks while preserving transport and magnetic functionality.

## Conceptual Foundation

MEAQ-T combines ideas from four active research frontiers:

1. **Moire thermoelectrics**
	- Twisted and lattice-mismatched interfaces produce minibands and flat-band features that can increase thermopower and tune carrier filtering.
2. **Twisted magnetic/skyrmion physics**
	- Interfacial frustration and moire modulation can stabilize nontrivial spin textures and pulse-addressable magnetic states.
3. **High-entropy materials**
	- Multicomponent disorder can improve phase robustness, damage tolerance, and thermal stability.
4. **Extreme-environment protective coatings**
	- Ceramic/metal/oxide architectures with graded interfaces and toughened matrices provide baseline survivability.

## Core Design Hypotheses

1. **Transport-plasticity coupling**
	- Moire miniband engineering can tune Seebeck response without fully sacrificing conductivity when coupled to entropy-stabilized host phases.
2. **Entropy-assisted reconfigurability**
	- High configurational entropy can widen metastable windows, enabling reversible pulse-driven state switching rather than catastrophic phase collapse.
3. **Spin-thermoelectric co-optimization**
	- Nanoscale magnetic textures can be leveraged to modulate local scattering and thermal transport pathways.
4. **Damage-adaptive functionality**
	- Self-healing chemistry and defect-migration channels can restore both mechanical continuity and functional pathways.

## Candidate Architecture

One possible multilayer stack:

1. **Top protective layer**
	- Chemically resistant barrier and radiation hardening.
2. **Adaptive active layer (MEAQ-T core)**
	- Twisted/interfacial heterostructure with entropy-stabilized composition.
3. **Pulse-coupling layer**
	- Designed for optical or thermal pulse absorption and fast energy delivery.
4. **Compliance/adhesion layer**
	- Thermal-expansion buffering and substrate bonding.
5. **Substrate interface engineering**
	- Defect sinks, graded chemistry, and crack-arrest structures.

## Simulation and Modeling Directions

Recommended multiphysics workflow:

1. **Electronic structure and transport**
	- Tight-binding/DFT-informed moire miniband models.
	- Boltzmann or NEGF transport estimates for thermoelectric figures of merit.
2. **Magnetic texture dynamics**
	- Micromagnetic simulations with interfacial DMI, anisotropy gradients, and pulse-driven switching.
3. **Entropy and phase stability**
	- CALPHAD-like high-entropy screening and kinetic Monte Carlo for metastable state persistence.
4. **Damage and healing kinetics**
	- Phase-field or continuum damage models coupled to defect diffusion and healing triggers.
5. **Extreme-environment reliability**
	- Thermal shock, radiation-induced defect generation, and corrosion stress tests in silico.

## Prototype Pathways

Potential early demonstrations:

1. **Thin-film coupon demonstrator**
	- Verify thermopower tunability vs twist/interfacial mismatch.
2. **Pulse-addressable magnetic tile**
	- Show reversible magnetic state switching under optical pulse trains.
3. **Damage-recovery coupon**
	- Introduce controlled microcracking, then measure electrical/thermal recovery.
4. **Harsh-environment chamber tests**
	- Co-validate protection, performance retention, and adaptation speed.

## Key Metrics

Target metric families to track:

1. Thermoelectric performance: Seebeck coefficient, power factor, effective $ZT$.
2. Reconfiguration: switching energy, switching time, cycle endurance.
3. Magnetic state control: retention, reversibility, skyrmion/topology stability.
4. Self-healing efficiency: crack closure fraction, property recovery ratio, repeatability.
5. Survivability: performance drift under thermal/radiation/chemical stress.

## Open Research Questions

1. Which composition spaces maximize both entropy stabilization and functional tunability?
2. How does moire-scale disorder affect transport coherence at operating temperatures?
3. What pulse windows achieve deterministic switching without irreversible damage?
4. Can healing pathways be triggered selectively without degrading electronic interfaces?
5. What architecture best balances protection with adaptive functionality?

## Repository Scope

This repository is intended to document:

1. Concept motivation and technical rationale
2. Design hypotheses and architecture options
3. Modeling and simulation plans
4. Experimental prototype strategies
5. Risk and validation frameworks

## Status

Current phase: **Concept and pre-prototype planning**.

Near-term next steps:

1. Define a baseline simulation stack and parameter ranges.
2. Select 2-3 candidate material systems for first-pass screening.
3. Draft benchmark experiments and failure criteria for feasibility gates.

## Practical Prototype Path

An implementation-first sequence aligned with the MEAQ-T concept:

1. Build and validate a self-healing extreme-environment base coating.
2. Integrate a high-entropy interlayer for phase stability and thermal management.
3. Transfer and encapsulate moire-active 2D stacks (for example twisted MoTe2/WSe2 in hBN).
4. Characterize gate, temperature, twist, and pulse dependence of thermoelectric and magnetic response.
5. Close the loop between simulation outputs and fabrication choices.

## Material Baselines (Actionable)

Two baseline protective routes are now encoded in the optimizer and can be compared side-by-side:

1. `bio_vitrimer_imine_sio2_2wt`
	- Intended for moderate-temperature self-healing prototypes.
	- Target healing window: ~80-120 C.
	- Example chemistry: methacrylated vanillin + flexible diamine + methacrylated eugenol + 2 wt% functionalized SiO2.
2. `hfb2_sic_tasi2_uhtc`
	- Intended for ultra-high-temperature ablation protection.
	- Example route: slurry/plasma deposition on SiC-prepared substrate, then sinter/oxidation conditioning.

Recommended high-entropy interlayers included in the optimizer:

1. `he_rocksalt_mg_co_ni_cu_zn_o`
2. `he_oxide_hf_zr_ta_nb_ti`
3. `he_perovskite_sr_la_nd_sm_eu_tio3`

Moiré active layer baseline:

1. `mote2_wse2_hbn` with low-angle twist (typically 0-5 degrees).

## Suggested Fabrication Sequence

1. Build and densify high-temperature structural layers first (substrate + UHTC/heavy ceramic layers when used).
2. Deposit high-entropy interlayer via Pechini/molten-salt/solid-state route and finish thermal treatments.
3. Assemble hBN / MoTe2-WSe2 / hBN using deterministic dry transfer at low temperature.
4. Apply low-temperature vitrimer topcoat (spin, dip, or spray) and UV-cure if using photocurable chemistry.
5. Run thermal cycling and healing assays before pulse-driven functional tests.

## Coating Optimization Presets

`scripts/run_coating_opt.py` supports objective presets:

1. `balanced`: general-purpose ranking.
2. `prototype_low_temp`: prioritizes healing and lower-process-risk paths.
3. `extreme_uht`: prioritizes high-temperature and radiation survivability.

Examples:

```bash
python scripts/run_coating_opt.py --preset prototype_low_temp --top-k 12
python scripts/run_coating_opt.py --preset extreme_uht --top-k 12
python scripts/run_coating_opt.py --preset balanced --score-mode normalized --top-k 12 --min-heat-tol 0.70 --max-thermal-kappa 2.0
python scripts/compare_coating_presets.py --left prototype_low_temp --right extreme_uht --top-k 12
python scripts/compare_coating_presets.py --left prototype_low_temp --right extreme_uht --score-mode normalized --min-healing-rate 0.30 --top-k 12
```

Comparison outputs:

1. `coating_preset_by_rank.csv`: direct rank-to-rank comparison.
2. `coating_preset_side_by_side.csv`: overlap-aware table keyed by stack identity.
3. `coating_preset_ranked.csv`: combined ranked list with preset label.

Useful optimizer controls:

1. `--score-mode normalized` for scale-balanced objective aggregation.
2. Feasibility filters: `--min-heat-tol`, `--min-radiation-tol`, `--min-healing-rate`, `--max-thermal-kappa`, `--min-coupling`.

## Research Timeline (Starter)

1. Literature and modeling (1-2 months): calibrate scaffold models with DFT/tight-binding inputs and screen 100+ high-entropy candidates.
2. Synthesis and fabrication: build coating stack iteratively (self-healing base -> HE interlayer -> moire active layer).
3. Characterization: Seebeck/Nernst vs gate and temperature, pump-probe pulse tests, and thermal cycling/healing retention.
4. Optimization: update composition, twist angle, and pulse windows from measured feedback.

## First Coding Scaffolds (Implemented)

This repository now includes four starter modules under `src/meaqt`:

1. `composition.py`
	- High-entropy composition screening.
	- Uses configurational entropy ($\Delta S_{mix}$), radius mismatch, melting-point, and electronegativity proxies.
2. `moire_transport.py`
	- Twist/displacement/temperature scans for conductivity, Seebeck, power-factor proxy, and Nernst proxy.
3. `pulse_response.py`
	- Ultrafast pulse-driven magnetic switching with a compact LLG model and optional topological-charge estimator.
4. `coating_optimizer.py`
	- Multi-objective stack ranking with optional Pareto filtering.

## Setup and Quickstart

Create an isolated environment and install in editable mode:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .[test]
```

Run the full scaffold workflow:

```bash
python scripts/run_composition_screen.py --n-elements 5 --top-k 20 --out composition_screen.csv
python scripts/run_moire_scan.py --filling 0.0 --out moire_scan.csv
python scripts/run_pulse_sim.py --amp -1.2 --duration 20
python scripts/run_coating_opt.py --top-k 12 --out coating_ranked.csv --out-pareto coating_pareto.csv
python scripts/run_plot_maps.py --out-dir figures --filling 0.1 --temp 50
python scripts/run_dft_extract.py data/benchmarks/vasp_sample.out --code auto --out dft_summary.csv
python scripts/run_pulse_phase_diagram.py --out-dir figures
pytest -q
```

## Validated Script Runs

The following commands were re-validated in this repository on 2026-07-14:

```bash
python scripts/run_coating_opt.py --preset balanced --top-k 12 --out /tmp/coating_ranked_balanced.csv --out-pareto /tmp/coating_pareto_balanced.csv
python scripts/run_coating_opt.py --preset prototype_low_temp --score-mode normalized --top-k 10 --min-healing-rate 0.30 --out /tmp/coating_ranked_proto.csv --out-pareto /tmp/coating_pareto_proto.csv
python scripts/run_coating_opt.py --preset extreme_uht --top-k 8 --min-heat-tol 0.75 --min-radiation-tol 0.70 --max-thermal-kappa 2.0 --out /tmp/coating_ranked_uht.csv --out-pareto /tmp/coating_pareto_uht.csv
python scripts/run_pulse_sim.py --amp -1.2 --duration 20
python scripts/run_moire_scan.py --filling 0.1 --out /tmp/moire_scan.csv
python scripts/compare_coating_presets.py --left prototype_low_temp --right extreme_uht --top-k 8
```

Observed outputs from the validation run:

1. `run_coating_opt.py` generated ranked and Pareto CSV outputs for all tested presets.
2. Constraint-heavy extreme-UHT settings produced a narrowed feasible set (2 rows), confirming filters are active.
3. `run_pulse_sim.py` reported switching (`switched=True`) with default pulse parameters.
4. `run_moire_scan.py` produced a 252-row grid scan with expected transport columns.
5. `compare_coating_presets.py` produced all comparison tables (`by_rank`, `side_by_side`, `ranked`).

## New Additions (This Iteration)

1. DFT adapters in `src/meaqt/dft_adapters.py` for lightweight VASP/QE parsing.
   - Includes confidence scoring, missing-field reporting, and parse notes.
2. Plotting helpers in `src/meaqt/plotting.py` for:
   - Seebeck and power-factor heatmaps
   - Pulse-driven magnetization trajectories
   - Pulse amplitude-width switching phase diagrams
   - Coating candidate scatter views
3. New scripts:
   - `scripts/run_plot_maps.py`
   - `scripts/run_dft_extract.py`
   - `scripts/run_pulse_phase_diagram.py`
4. Benchmark fixtures and tests:
   - `data/benchmarks/vasp_sample.out`
   - `data/benchmarks/qe_sample.out`
   - `data/benchmarks/expected_ranges.json`
   - `data/benchmarks/coating_preset_golden.json`
   - `tests/test_scaffolds.py`

## Notes on Model Scope

These are intentionally lightweight research scaffolds, not calibrated production solvers.

1. Replace toy minibands in the moire module with DFT-derived dispersions.
2. Replace macrospin pulse model with atomistic or micromagnetic spatial solvers for skyrmion dynamics.
3. Expand high-entropy scoring with CALPHAD/ML phase predictions and measured transport datasets.
4. Connect optimizer objectives to experimentally measured durability and healing kinetics.
