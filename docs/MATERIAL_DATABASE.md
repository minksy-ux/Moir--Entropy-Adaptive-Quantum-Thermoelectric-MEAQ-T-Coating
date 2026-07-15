# MEAQ-T Coating: Material Database Enhancement Plan

**Status**: Roadmap for expanding element database and integrating material properties  
**Last Updated**: 2026-07-15  
**Current Coverage**: 11 elements (Hf, Zr, Ta, Nb, Ti, Mo, W, Si, Al, Y, Yb)  
**Target Coverage**: 30+ elements by end of Year 1

---

## Executive Summary

The current ELEMENT_DB (in `src/meaqt/composition.py`) contains basic atomic parameters for 11 refractory elements. This document outlines expansion to 30+ elements with **temperature-dependent properties**, **phase diagram information**, **experimental transport data**, and **supplier / cost information**.

---

## Current ELEMENT_DB Structure (Python)

```python
ELEMENT_DB = {
    'Hf': {'mass': 178.49, 'radius': 1.75, 'valence': 4, ...},
    'Zr': {'mass': 91.224, 'radius': 1.60, 'valence': 4, ...},
    # ... 9 more elements
}
```

**Limitations**:
- Static properties only (no T-dependence)
- No phase information
- No cost data
- Limited electronegativity detail

---

## Proposed Enhanced Database Structure

### 1. Expanded Element Coverage (30 elements)

**Group 1: Refractory Metals (HEA-prime)**
- Hf, Zr, Ti, V, Nb, Ta, Mo, W, Cr, Mn

**Group 2: Transition Metals (Secondary)**
- Co, Ni, Cu, Fe, Ru, Re, Os, Ir, Pt, Pd

**Group 3: Rare Earths & Lanthanides (Optional)**
- La, Ce, Y, Yb, Gd (for entropy enhancement)

**Group 4: Light Metals & Semimetals (Functional)**
- Al, Si, Sn, Ge (for ceramics, thermal properties)

**Group 5: Chalcogens & Pnictogens (2D layer components)**
- Te, Se, S, P, As (for heterostructure doping)

### 2. Enhanced Property Fields

For each element, store:

```python
ELEMENT_DB_ENHANCED = {
    'Hf': {
        # Atomic
        'atomic_number': 72,
        'mass': 178.49,  # g/mol
        'radius_metallic': 1.75,  # Angstrom
        'radius_ionic_4p': 0.84,  # Å (4+ oxidation state)
        'electroneg_pauling': 1.3,
        
        # Static (300 K)
        'valence': 4,
        'common_oxidation_states': [2, 3, 4],
        'density_metal': 13.3,  # g/cm³
        'density_oxide': 9.68,  # g/cm³ (HfO₂)
        'density_carbide': 12.7,  # g/cm³ (HfC)
        
        # Thermodynamic & Transport (300 K baseline, function T)
        'melting_point': 2506,  # K
        'boiling_point': 4876,
        'specific_heat_metal': 0.144,  # J/g-K (300 K)
        'thermal_conductivity_metal': 0.23,  # W/cm-K at 300 K
        'electrical_conductivity_metal': 3.8e5,  # S/m at 300 K
        'thermal_expansion_coeff': 5.9e-6,  # 1/K (average 298-373 K)
        
        # Oxide Properties
        'thermal_conductivity_oxide': 0.023,  # W/cm-K (HfO₂, 300 K)
        'band_gap_oxide': 5.9,  # eV (HfO₂)
        
        # Temperature-Dependent Models (polynomials or lookup tables)
        'cp_model': {'type': 'polynomial', 'coeffs': [...]},  # Shomate coefficients
        'thermal_cond_model': {'type': 'power_law', 'params': {'a': 0.23, 'b': -0.5}},  # κ(T) = a * T^b
        
        # Phase Information
        'crystal_structures': {
            'α': {'structure': 'hcp', 'stable_range': [0, 1596]},  # Temperature range in K
            'β': {'structure': 'bcc', 'stable_range': [1596, 2506]}
        },
        
        # Supplier & Cost
        'typical_purity': 99.9,  # %
        'typical_cost_per_kg': 150,  # USD (2026), oxide form
        'suppliers': [
            {'name': 'Sigma-Aldrich', 'code': 'H4,018-1', 'form': 'powder', 'price_per_kg': 250},
            {'name': 'Alfa Aesar', 'code': '41969', 'form': 'powder', 'price_per_kg': 200}
        ]
        
        # Reference Data & Source
        'references': {
            'thermal_cond': {'source': 'Touloukian et al., TPRC (1970)', 'doi': '...'},
            'phase_diagram': {'source': 'ASM Handbook', 'volume': 15},
            'transport': {'source': 'Kittel & Kroemer', 'doi': '...'}
        }
    },
    # ... repeat for 30 elements
}
```

---

## Implementation Roadmap

### Phase 1 (Weeks 1–4): Data Collection & Compilation

**Task 1.1: Atomic parameters** (Week 1)
- Source: NIST, CRC Handbook, Webelements.com
- Collect for all 30 elements: atomic mass, radii, electronegativity, valence
- Output: CSV template + entries

**Task 1.2: Static properties @ 300 K** (Week 2)
- Melting/boiling points: Literature search
- Density (metal, oxide, carbide forms): Compile from sources
- Specific heat: Shomate database (JANAF thermochemical tables)
- Thermal conductivity & electrical conductivity: Materials databases

**Task 1.3: Temperature-dependent models** (Weeks 2–3)
- Shomate coefficients (C_p vs. T) from NIST-JANAF database
- Thermal conductivity polynomial fits: Power law κ = a × T^b
- Linear CTE models: α(T) ≈ α₀ × (1 + β × ΔT)
- Output: Polynomial coefficients table

**Task 1.4: Phase diagrams** (Week 3)
- Collect phase data: Crystal structures, stable temperature ranges
- Focus on elements in HEA compositions (Hf-Zr-Ta-Nb-Ti phase diagram)
- Source: ASM Handbook, CALPHAD databases

**Task 1.5: Supplier & cost** (Week 4)
- Survey 3–5 suppliers (Sigma-Aldrich, Alfa Aesar, ChemPure, Noah Chemicals)
- Typical purity levels & form (powder, granule, lump)
- 2026 pricing
- Output: Supplier list with contact info

**Deliverable**: Comprehensive spreadsheet (30 elements × 40+ properties)

### Phase 2 (Weeks 5–8): Data Quality & Validation

**Task 2.1: Cross-validation**
- Compare multiple sources for each property
- Flag discrepancies (>10% difference)
- Prioritize peer-reviewed sources over commercial databases

**Task 2.2: Temperature-dependent fitting**
- Fit polynomial models to experimental data
- Validate fits against 5–10 intermediate points
- Estimate uncertainty ranges

**Task 2.3: Phase diagram assembly**
- Compile Hf-Zr, Hf-Ta, Zr-Ta binary diagrams
- Extract congruent melting points, eutectic temperatures
- Ternary diagrams (Hf-Zr-Ta) from literature

**Deliverable**: Validated dataset, uncertainty quantification

### Phase 3 (Weeks 9–12): Code Implementation

**Task 3.1: Python data structure**
```python
# Updated ELEMENT_DB_ENHANCED in meaqt/element_database.py
ELEMENT_DB_ENHANCED = {
    'Hf': { ... },  # As defined above
    # ... 29 more elements
}

# Helper functions
def get_property(element, property_name, temperature=300):
    """Return property value at given temperature, interpolating if needed."""
    ...

def get_thermal_conductivity(element, temp_K):
    """Return κ(T) using polynomial model."""
    ...

def suggest_compositions(n_elements, target_properties):
    """Screen compositions based on cost, density, entropy, desired properties."""
    ...
```

**Task 3.2: Integration with existing modules**
- Update `composition.py`: Use enhanced element database for screening
- Update `moire_transport.py`: Access T-dependent transport properties
- Add new functions: `cost_analysis()`, `phase_stability_check()`

**Task 3.3: Database versioning**
- Git version control: Track changes to ELEMENT_DB
- Release versions: v1.0 (30 elements), v1.1 (added DFT validation), etc.

**Deliverable**: `element_database.py` module with 30 elements + helper functions

### Phase 4 (Weeks 13–16): Experimental Validation & Iteration

**Task 4.1: Compare predictions to literature**
- Pick 5 test compounds (e.g., HfO₂, ZrO₂, HfB₂)
- Predict transport properties using enhanced database
- Compare to published experimental values
- Adjust models if needed

**Task 4.2: Field feedback**
- Distribute to early users (collaborators, students)
- Gather feedback on usability, accuracy, missing properties
- Iterate: Add high-priority missing properties

**Deliverable**: Validated model v1.0, feedback summary, published data

---

## Data Sources (Prioritized)

| Property | Primary Source | Secondary | Tertiary |
|---|---|---|---|
| **Atomic parameters** | NIST, Webelements | CRC Handbook | Mendeleev Dashboard |
| **Melting point** | ASM Handbook Vol. 15 | TPRC (NIST) | DOE Materials Data |
| **Density** | CRC Handbook | MatWeb | Calculated from lattice constants |
| **Specific heat** | JANAF Thermochemical Tables | NIST-WEBBOOK | Dulong-Petit estimate (low-T) |
| **Thermal conductivity** | Touloukian et al. (TPRC) | PMAT database | Wiedemann-Franz law (estimate from σ) |
| **Electrical conductivity** | CRC Handbook | PMAT | Calculated from resistivity data |
| **CTE** | Touloukian, Vol. 12 | ASM | Linear extrapolation from ΔL/L|
| **Phase diagrams** | ASM Handbook Vol. 3 | CALPHAD databases | Thermo-Calc (institution license) |
| **Cost** | Supplier websites | ChemLogo | Average of 3+ quotes |

---

## Data Quality Metrics

For each element & property:
- **Confidence score** (0–100%): Based on number of independent sources
- **Uncertainty range**: ±X% (estimate based on literature scatter)
- **Last updated**: Date of most recent literature or supplier check

**Target Confidence Levels**:
- **Atomic parameters**: 95%+ (well-established)
- **Thermal conductivity**: 80–90% (varies with sample, orientation)
- **Cost**: 90%+ (updated quarterly)
- **Phase data**: 85%+ (from ASM Handbook)
- **T-dependent models**: 70–85% (extrapolation uncertainty increases with |T - 300K|)

---

## New Utility Functions

### 1. Cost-Benefit Analysis

```python
def analyze_composition_cost_benefit(composition_dict, target_properties):
    """
    Input: {'Hf': 0.2, 'Zr': 0.2, 'Ta': 0.2, 'Nb': 0.2, 'Ti': 0.2}
           target_properties = {'min_melting_point': 2000, 'max_density': 10}
    Output: {
        'total_cost_per_kg': 150,
        'weighted_entropy': 1.6,
        'target_compliance': [True, False],  # Which targets met
        'recommendation': 'Good, low-cost high-entropy candidate'
    }
    """
    ...
```

### 2. Temperature-Dependent Property Lookup

```python
def get_transport_tensor(composition, temperature_K, property='thermal_conductivity'):
    """
    Input: composition dict, T in K, property name
    Output: Property value at temperature using T-dependent model
    """
    ...
```

### 3. Phase Stability Check

```python
def check_phase_stability(composition, temperature_K):
    """
    Input: Equiatomic composition, operating temperature
    Output: 'Single phase stable', 'Expected phase separation at T_sep', etc.
    """
    ...
```

### 4. Supplier Comparison

```python
def find_best_supplier(element, purity_min=99.9, quantity_kg=1, form='powder'):
    """
    Query supplier database, return best price & lead time
    """
    ...
```

---

## Integration with Existing Project Code

### `src/meaqt/composition.py` Updates

```python
# OLD:
ELEMENT_DB = {
    'Hf': {'mass': 178.49, 'radius': 1.75, 'valence': 4},
    ...
}

# NEW:
from meaqt.element_database import ELEMENT_DB_ENHANCED

# Use enhanced properties in screening:
def screen_compositions(n_elements=4, constraints=None):
    """
    Enhanced version with cost, phase stability filters
    """
    candidates = []
    for composition in generate_candidates(n_elements):
        # NEW: Check cost
        cost = calculate_composition_cost(composition, ELEMENT_DB_ENHANCED)
        if cost > budget_constraint:
            continue
        
        # NEW: Check phase stability at operating temp
        phase_status = check_phase_stability(composition, 1000)  # 1000 K
        if 'separator' in phase_status:
            risk_score += 10
        
        # Existing logic
        entropy = config_entropy(composition, ELEMENT_DB)
        ...
        candidates.append((composition, score))
    
    return candidates
```

### `src/meaqt/moire_transport.py` Updates

```python
# Access temperature-dependent properties
def scan_moire_response(composition, temperatures=[300, 600, 1000]):
    """
    Scan Seebeck, power factor across temperatures
    """
    results = []
    for T in temperatures:
        # Get T-dependent thermal conductivity
        kappa_T = get_thermal_conductivity(composition, T, ELEMENT_DB_ENHANCED)
        
        # Calculate transport properties
        seebeck = calculate_seebeck(composition, T, kappa_T)
        ...
        results.append((T, seebeck, ...))
    
    return results
```

---

## Documentation & User Guide

### README Section: Using the Material Database

```markdown
## Material Database

The MEAQ-T project includes an enhanced material database with 30 elements.

### Quick Start

```python
from meaqt.element_database import ELEMENT_DB_ENHANCED, get_thermal_conductivity

# Get thermal conductivity of Hf at 800 K
kappa = get_thermal_conductivity('Hf', 800)  # W/cm-K

# Check phase stability
from meaqt.element_database import check_phase_stability
phase_status = check_phase_stability({'Hf': 0.3, 'Zr': 0.3, 'Ta': 0.2, 'Nb': 0.2}, 1200)
```

### Properties Available

- Atomic parameters (mass, radius, electronegativity)
- Density (metal, oxide, carbide forms)
- Melting/boiling points
- Thermal conductivity vs. temperature
- Electrical conductivity vs. temperature
- Specific heat vs. temperature
- Phase diagram information
- Supplier & cost data

### Data Quality

All properties include:
- Confidence score (%)
- Uncertainty estimate (±%)
- Source reference
- Last update date

See [MATERIAL_DATABASE.md](docs/MATERIAL_DATABASE.md) for detailed property tables.
```

---

## Long-Term Roadmap (Year 2+)

### Advanced Features

**1. Machine Learning Integration**
- Train ML model to predict missing properties (e.g., Seebeck from atomic parameters)
- Uncertainty quantification: Bayesian model
- Extrapolation beyond current element set

**2. DFT Validation**
- Compute thermal conductivity of oxides via DFT + Boltzmann transport
- Compare to ELEMENT_DB values, refine if needed
- Uncertainty bands: experiment ± DFT estimate

**3. Real-Time Updates**
- Web scraping of supplier prices (quarterly)
- Integration with NIST databases via API
- Version control: Automatic database updates with timestamp

**4. Export Formats**
- JSON (for web apps)
- HDF5 (for large simulations)
- Excel (for manual inspection)

---

## References & Related Documents

- [Synthesis Protocol](SYNTHESIS_PROTOCOL.md): Material sourcing info
- [Computational Roadmap](COMPUTATIONAL_ROADMAP.md): DFT validation of thermal properties
- [Literature Database](LITERATURE.md): Source publications for property data
- NIST-JANAF Thermochemical Tables: https://janaf.nist.gov
- ASM Handbook Volume 15 (Casting): Phase diagrams
