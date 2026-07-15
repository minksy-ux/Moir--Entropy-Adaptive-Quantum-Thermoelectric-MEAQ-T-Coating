# MEAQ-T Jupyter Notebooks

Interactive tutorials for the MEAQ-T modeling and optimization platform.

## Notebooks

### 1. Quickstart: 01_quickstart.ipynb
**Duration**: 5–10 minutes | **Level**: Beginner

Complete end-to-end workflow:
- High-entropy composition screening
- Moire transport characterization
- Pulse-driven magnetic switching simulation
- Coating stack optimization
- Publication-ready visualizations

**Key functions used**:
- `screen_compositions()` → filter HEAs by entropy and thermal proxies
- `scan_moire_response()` → compute Seebeck, power factor, etc.
- `simulate_pulse_switching()` → LLG dynamics with optical pulses
- `optimize_stacks()` → multi-objective coating design
- Plotting utilities

### 2. Advanced: 02_advanced_optimization.ipynb
**Duration**: 10 minutes | **Level**: Intermediate

Multi-scenario analysis and Pareto optimization:
- Compare weight presets (balanced, UHT, prototype)
- Apply hard constraints (thermal conductivity, coupling strength)
- Extract Pareto-optimal non-dominated solutions
- Trade-off visualization and interpretation

**Key concepts**:
- Preset-based re-weighting for different applications
- Constraint-satisfaction filtering
- Pareto front identification

### 3. DFT Integration: 03_dft_parsing.ipynb
**Duration**: 5 minutes | **Level**: Intermediate

Parse and integrate DFT outputs:
- Auto-detect VASP vs. Quantum ESPRESSO format
- Extract Fermi level, total energy, band gap
- Confidence scoring and diagnostic notes
- Batch processing multiple calculations

**Key functions used**:
- `parse_dft_text()` / `parse_dft_report()` → auto-detection and parsing
- Confidence assessment
- Error/missing-field reporting

## Running the Notebooks

### Option 1: JupyterLab (Recommended)
```bash
cd /path/to/repo
python -m venv .venv
source .venv/bin/activate
pip install -e .[test]
jupyter lab notebooks/
```

### Option 2: Jupyter Notebook
```bash
jupyter notebook notebooks/01_quickstart.ipynb
```

### Option 3: VS Code
- Install the Jupyter extension (ms-toolsai.jupyter)
- Open any `.ipynb` file in VS Code
- Run cells interactively

## How to Use

1. **Start with 01_quickstart.ipynb** to understand the full workflow.
2. **Proceed to 02_advanced_optimization.ipynb** for advanced scenarios.
3. **Use 03_dft_parsing.ipynb** when integrating DFT data.

Each notebook is self-contained and can run independently, but they use common data formats and module APIs.

## Troubleshooting

### "Module meaqt not found"
Make sure you've installed the package in editable mode:
```bash
pip install -e .
```

Or manually add the src path in the notebook cell before importing:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd().parent / 'src'))
```

### Plots not showing
Ensure matplotlib backend is set correctly. Add to notebook:
```python
%matplotlib inline
```

### Performance / Memory issues
- Reduce `top_k` parameter in `optimize_stacks()` or `screen_compositions()`
- Use coarser grids for `scan_moire_response()`
- Subsample compositions before optimization

## Contributing

To add a new notebook:
1. Create a clear, self-contained tutorial
2. Use descriptive markdown cells with explanations
3. Include comments in code cells
4. Test with a fresh kernel (Kernel → Restart & Run All)
5. Name following pattern: `NN_description.ipynb`

## References

- Main API: `src/meaqt/__init__.py`
- Theory & Design: `README.md`
- Novelty & Evidence: `docs/novelty_evidence_map.md`
