"""
volumetric_validation.py

Place this script in a part folder alongside the two STL files and run it:
    python volumetric_validation.py

Requires:
    pip install numpy-stl

Expected files in the same folder as this script:
    source_<anything>.stl  — the original source STL
    <anything>.stl         — the output/printed STL (any other .stl in the folder)
"""

import logging
from datetime import datetime
from pathlib import Path

import numpy as np
from stl import mesh


# ── Logging setup ─────────────────────────────────────────────────────────────

def setup_logging(folder: Path, log_file: str):
    log = logging.getLogger("vol_validation")
    log.setLevel(logging.DEBUG)
    fmt = logging.Formatter("%(asctime)s  %(levelname)-8s  %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S")
    fh = logging.FileHandler(folder / log_file, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(fmt)
    log.addHandler(fh)
    log.addHandler(ch)
    return log


# ── Volume calculation ────────────────────────────────────────────────────────

def signed_volume_of_triangle(v0, v1, v2):
    return np.dot(v0, np.cross(v1, v2)) / 6.0


def compute_volume_from_file(stl_path: Path) -> float:
    m = mesh.Mesh.from_file(str(stl_path))
    total = 0.0
    for triangle in m.vectors:
        total += signed_volume_of_triangle(triangle[0], triangle[1], triangle[2])
    return abs(total)


# ── STL discovery ─────────────────────────────────────────────────────────────

def find_stl_pair(folder: Path, log):
    all_stls = list(folder.glob("*.stl"))

    source_files = [f for f in all_stls if f.name.startswith("source_")]
    output_files = [f for f in all_stls if not f.name.startswith("source_")]

    if not source_files:
        log.error("No source STL found (expected a file named source_*.stl).")
        return None, None
    if len(source_files) > 1:
        log.error(f"Multiple source STLs found: {[f.name for f in source_files]}. Expected exactly one.")
        return None, None

    if not output_files:
        log.error("No output STL found (expected a non-source_* .stl file).")
        return None, None
    if len(output_files) > 1:
        log.error(f"Multiple output STLs found: {[f.name for f in output_files]}. Expected exactly one.")
        return None, None

    return source_files[0], output_files[0]


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    folder   = Path(__file__).parent.resolve()
    log_file = "volumetric_validation.log"
    log      = setup_logging(folder, log_file)

    log.info("=" * 60)
    log.info(f"volumetric_validation.py started — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info(f"Folder : {folder}")

    source_path, output_path = find_stl_pair(folder, log)
    if not source_path or not output_path:
        log.error("Place source_<name>.stl and <name>.stl in the same folder and re-run.")
        return

    log.info(f"Source STL : {source_path.name}")
    log.info(f"Output STL : {output_path.name}")

    # ── Volume comparison ─────────────────────────────────────────────────────
    try:
        vol_source = compute_volume_from_file(source_path)
        vol_output = compute_volume_from_file(output_path)

        abs_diff = abs(vol_output - vol_source)
        pct_diff = (abs_diff / vol_source * 100) if vol_source != 0 else float("inf")

        log.info(f"Source volume : {vol_source:.2f} mm³")
        log.info(f"Output volume : {vol_output:.2f} mm³")
        log.info(f"Difference    : {abs_diff:.2f} mm³  ({pct_diff:.2f}%)")

    except Exception as e:
        log.error(f"Failed to compute volume: {e}")

    log.info("=" * 60)
    log.info(f"Log saved to: {folder / log_file}")


if __name__ == "__main__":
    main()
