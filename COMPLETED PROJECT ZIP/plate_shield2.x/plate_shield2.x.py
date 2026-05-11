from build123d import *
from ocp_vscode import show
import csv, math, os

# =========================
# FILE
# =========================
csv_path = os.path.expanduser("~/Desktop/plate_shield2.x.csv")

# =========================
# READ CSV
# =========================
points = []
with open(csv_path, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        x_val = row.get("X") or row.get("x")
        y_val = row.get("Y") or row.get("y")
        if x_val and y_val:
            points.append((float(x_val), float(y_val)))

print("Points Loaded:", len(points))

# =========================
# SORT POINTS
# =========================
cx = sum(p[0] for p in points) / len(points)
cy = sum(p[1] for p in points) / len(points)
outer = sorted(points, key=lambda p: math.atan2(p[1]-cy, p[0]-cx))

# =========================
# HOLES
# =========================
holes = [
    (-33.4383, 60, 2, 4),
    (57, 21.7686, 2, 4),
    (57.5617, -60, 2, 4),
    (0.28, -74.5803, 2, 4),
    (-45.5294, -58.7, 2, 2),
    (-32.0294, -55.2, 2, 2),
    (-58.0209, -32.3463, 2, 4),
    (-56.4383, 17, 2, 4),
]

# =========================
# CIRCULAR CUTS
# =========================
circular_cuts = [
    (-50.3131, -72.9967),
    (58.5350, -47.9933),
    (57.5509, 9.8700),
    (16.1326, 53.6068),
    (-45.4701, 59.0035),
    (-73.2961, 37.0531),
]

# =========================
# BUILD PART
# =========================
with BuildPart() as part:

    with BuildSketch() as sk:
        with BuildLine():
            Polyline(*outer, close=True)
        make_face()

    # Plate thickness
    extrude(sk.sketch, amount=2.0)

    # Tapered holes
    for hx, hy, r_bot, r_top in holes:
        with BuildSketch(Plane.XY) as bot:
            with Locations((hx, hy)):
                Circle(r_bot)

        with BuildSketch(Plane.XY.offset(4)) as top:
            with Locations((hx, hy)):
                Circle(r_top)

        loft([bot.sketch, top.sketch], mode=Mode.SUBTRACT)

# =========================
# FINAL SOLID
# =========================
result = part.part

# =========================
# CYLINDER CUTS
# =========================
for hx, hy in circular_cuts:
    cyl = Cylinder(radius=5, height=2.5)
    cyl = cyl.moved(Location((hx, hy, 4 - 1.25)))
    result = result - cyl
# SHOW
show(result, reset_camera=True)

# EXPORT
stl_path = csv_path.replace(".csv", ".stl")
export_stl(result, stl_path)

print("✅ STL saved:", stl_path)