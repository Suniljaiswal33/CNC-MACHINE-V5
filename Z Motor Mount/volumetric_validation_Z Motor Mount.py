"""
volumetric_validation.py

Download this script into a part folder and run it alongside the two STL files:
    python volumetric_validation_<PartName>.py

Requires:
    pip install numpy-stl

Expected files in the same folder as this script:
    <PartName>.stl          — the output/printed STL
    source_<PartName>.stl  — the original source STL
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


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    folder   = Path(__file__).parent.resolve()
    stem     = Path(__file__).stem                          # e.g. volumetric_validation_MyPart
    part_name = stem.replace("volumetric_validation_", "", 1)  # e.g. MyPart
    log_file = stem + ".log"
    log      = setup_logging(folder, log_file)

    log.info("=" * 60)
    log.info(f"{stem}.py started — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info(f"Part name  : {part_name}")
    log.info(f"Folder     : {folder}")

    output_path = folder / f"{part_name}.stl"
    source_path = folder / f"source_{part_name}.stl"

    # ── File presence checks ──────────────────────────────────────────────────
    missing = []
    if not output_path.exists():
        missing.append(str(output_path.name))
    if not source_path.exists():
        missing.append(str(source_path.name))

    if missing:
        for name in missing:
            log.error(f"File not found: {name}")
        log.error("Place both STL files in the same folder as this script and re-run.")
        return

    log.info(f"Output STL : {output_path.name}")
    log.info(f"Source STL : {source_path.name}")

    # ── Volume comparison ─────────────────────────────────────────────────────
    try:
        vol_output = compute_volume_from_file(output_path)
        vol_source = compute_volume_from_file(source_path)

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
