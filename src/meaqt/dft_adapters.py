from __future__ import annotations

from dataclasses import dataclass
import re

RY_TO_EV = 13.605693009


@dataclass(frozen=True)
class DFTSummary:
    code: str
    fermi_ev: float | None
    total_energy_ev: float | None
    band_gap_ev: float | None


@dataclass(frozen=True)
class DFTParseReport:
    summary: DFTSummary
    confidence: float
    missing_fields: tuple[str, ...]
    notes: tuple[str, ...]


def _extract_float(pattern: str, text: str) -> float | None:
    match = re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE)
    if not match:
        return None
    return float(match.group(1))


def parse_vasp_text(text: str) -> DFTSummary:
    fermi_ev = _extract_float(r"E-fermi\s*:\s*([-+]?\d*\.?\d+)", text)
    total_energy_ev = _extract_float(r"free\s+energy\s+TOTEN\s*=\s*([-+]?\d*\.?\d+)", text)

    # Lightweight gap estimate if user has post-processed lines in text.
    band_gap_ev = _extract_float(r"band\s+gap\s*[:=]\s*([-+]?\d*\.?\d+)", text)
    return DFTSummary(
        code="vasp",
        fermi_ev=fermi_ev,
        total_energy_ev=total_energy_ev,
        band_gap_ev=band_gap_ev,
    )


def parse_qe_text(text: str) -> DFTSummary:
    fermi_ev = _extract_float(r"the\s+fermi\s+energy\s+is\s+([-+]?\d*\.?\d+)\s+ev", text)
    total_energy_ry = _extract_float(r"!\s+total\s+energy\s*=\s*([-+]?\d*\.?\d+)\s+Ry", text)
    total_energy_ev = total_energy_ry * RY_TO_EV if total_energy_ry is not None else None
    band_gap_ev = _extract_float(r"band\s+gap\s*[:=]\s*([-+]?\d*\.?\d+)", text)
    return DFTSummary(
        code="qe",
        fermi_ev=fermi_ev,
        total_energy_ev=total_energy_ev,
        band_gap_ev=band_gap_ev,
    )


def parse_dft_text(text: str, code: str = "auto") -> DFTSummary:
    code_norm = code.strip().lower()
    if code_norm == "vasp":
        return parse_vasp_text(text)
    if code_norm in {"qe", "espresso", "quantum-espresso"}:
        return parse_qe_text(text)

    # Auto-detect using signature patterns.
    if re.search(r"E-fermi\s*:", text, flags=re.IGNORECASE):
        return parse_vasp_text(text)
    if re.search(r"the\s+fermi\s+energy\s+is", text, flags=re.IGNORECASE):
        return parse_qe_text(text)
    raise ValueError("Unable to detect DFT code. Pass --code vasp or --code qe.")


def build_parse_report(summary: DFTSummary) -> DFTParseReport:
    missing = []
    notes = []
    if summary.fermi_ev is None:
        missing.append("fermi_ev")
    if summary.total_energy_ev is None:
        missing.append("total_energy_ev")
    if summary.band_gap_ev is None:
        missing.append("band_gap_ev")
        notes.append("band_gap_ev absent; provide post-processed gap line for deterministic extraction")

    confidence = 0.0
    confidence += 0.45 if summary.fermi_ev is not None else 0.0
    confidence += 0.45 if summary.total_energy_ev is not None else 0.0
    confidence += 0.10 if summary.band_gap_ev is not None else 0.0

    if summary.total_energy_ev is not None and summary.total_energy_ev > 0.0:
        notes.append("total_energy_ev is positive; verify parser target and unit conversion")
        confidence *= 0.8

    return DFTParseReport(
        summary=summary,
        confidence=float(max(0.0, min(1.0, confidence))),
        missing_fields=tuple(missing),
        notes=tuple(notes),
    )


def parse_dft_report(text: str, code: str = "auto") -> DFTParseReport:
    return build_parse_report(parse_dft_text(text=text, code=code))
