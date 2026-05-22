from build123d import *
from pathlib import Path
import numpy as np

# =====================================================
# PART NAME
# =====================================================
part_name = "Y Axis Motor Mount and Slider"

# =====================================================
# SVD PLANE CALCULATION FROM 6 POINTS (EXISTING)
# =====================================================
svd_plane_pts_3d = [
    (56.75, -0.59, 7.66),
    (50.02, 2.22, 10.47),
    (43.15, -0.69, 7.56),
    (43.15, -6.03, 2.21),
    (49.75, -8.85, -0.60),
    (56.75, -6.03, 2.21),
]

# Calculate plane normal from first 3 points
pt1 = np.array(svd_plane_pts_3d[0])
pt2 = np.array(svd_plane_pts_3d[1])
pt3 = np.array(svd_plane_pts_3d[2])

vec1 = pt2 - pt1
vec2 = pt3 - pt1
normal = np.cross(vec1, vec2)
normal = normal / np.linalg.norm(normal)

a, b, c = normal
d = np.dot(normal, pt1)

print("=" * 60)
print("SVD PLANE CALCULATION (EXISTING)")
print("=" * 60)
print(f"Normal = [{a:.8f}, {b:.8f}, {c:.8f}]")
print(f"Plane Equation: {a:.8f}x + {b:.8f}y + {c:.8f}z = {d:.8f}")
print("=" * 60)

# =====================================================
# NEW SVD PLANE CALCULATION FROM USER-PROVIDED POINTS
# =====================================================
new_svd_plane_pts = [
    (90.13, -1.38, 18.55),
    (-90.00, -1.38, 18.55),
    (-90.00, 9.98, 7.19),
    (90.00, 8.99, 8.18),
]

# Calculate plane from first 3 points
new_pt1 = np.array(new_svd_plane_pts[0])
new_pt2 = np.array(new_svd_plane_pts[1])
new_pt3 = np.array(new_svd_plane_pts[2])

new_vec1 = new_pt2 - new_pt1
new_vec2 = new_pt3 - new_pt1
new_normal = np.cross(new_vec1, new_vec2)
new_normal = new_normal / np.linalg.norm(new_normal)

new_a, new_b, new_c = new_normal
new_d = np.dot(new_normal, new_pt1)

print("\n" + "=" * 60)
print("NEW SVD PLANE CALCULATION (USER-PROVIDED)")
print("=" * 60)
print(f"Normal = [{new_a:.8f}, {new_b:.8f}, {new_c:.8f}]")
print(f"Plane Equation: {new_a:.8f}x + {new_b:.8f}y + {new_c:.8f}z = {new_d:.8f}")
print("=" * 60)

# =====================================================
# HEXAGON SVD PLANE CALCULATION FROM 6 POINTS
# =====================================================
hexagon_svd_pts = [
    (106.66, 26.38, 45.94),
    (-116.39, 22.78, 42.34),
    (-110.00, -52.21, -32.65),
    (91.41, -55.41, -35.85),
    (49.86, -9.03, 10.53),
    (-75.15, -9.03, 10.53),
]

# Calculate best-fit plane using SVD from all 6 points
points_matrix = np.array(hexagon_svd_pts)

# Center the points
centroid = np.mean(points_matrix, axis=0)
centered_points = points_matrix - centroid

# Perform SVD
U, S, Vt = np.linalg.svd(centered_points)

# Normal vector is the last row of Vt (smallest singular value)
hex_plane_normal = Vt[-1]
hex_plane_normal = hex_plane_normal / np.linalg.norm(hex_plane_normal)

hex_a, hex_b, hex_c = hex_plane_normal
hex_d = np.dot(hex_plane_normal, centroid)

print("\n" + "=" * 60)
print("HEXAGON SVD PLANE CALCULATION (6 POINTS)")
print("=" * 60)
print(f"Normal = [{hex_a:.8f}, {hex_b:.8f}, {hex_c:.8f}]")
print(f"Plane Equation: {hex_a:.8f}x + {hex_b:.8f}y + {hex_c:.8f}z = {hex_d:.8f}")
print(f"Centroid = [{centroid[0]:.6f}, {centroid[1]:.6f}, {centroid[2]:.6f}]")
print("=" * 60)

# =====================================================
# NEW SVD PLANE FROM 3 USER POINTS FOR HEXAGON CUTS
# Point 1: (75.00, -0.01, 9.89)
# Point 2: (-50.00, -0.01, 9.89)
# Point 3: (-56.69, -3.03, 12.90)
# =====================================================
hexagon_3pt_svd = [
    (75.00, -0.01, 9.89),
    (-50.00, -0.01, 9.89),
    (-56.69, -3.03, 12.90),
]

hex_3pt_pt1 = np.array(hexagon_3pt_svd[0])
hex_3pt_pt2 = np.array(hexagon_3pt_svd[1])
hex_3pt_pt3 = np.array(hexagon_3pt_svd[2])

hex_3pt_vec1 = hex_3pt_pt2 - hex_3pt_pt1
hex_3pt_vec2 = hex_3pt_pt3 - hex_3pt_pt1
hex_3pt_normal = np.cross(hex_3pt_vec1, hex_3pt_vec2)
hex_3pt_normal = hex_3pt_normal / np.linalg.norm(hex_3pt_normal)

hex_3pt_a, hex_3pt_b, hex_3pt_c = hex_3pt_normal
hex_3pt_d = np.dot(hex_3pt_normal, hex_3pt_pt1)

print("\n" + "=" * 60)
print("HEXAGON SVD PLANE - 3 POINT CALCULATION (USER POINTS)")
print("=" * 60)
print(f"Point 1: {hex_3pt_pt1}")
print(f"Point 2: {hex_3pt_pt2}")
print(f"Point 3: {hex_3pt_pt3}")
print(f"Normal = [{hex_3pt_a:.8f}, {hex_3pt_b:.8f}, {hex_3pt_c:.8f}]")
print(f"Plane Equation: {hex_3pt_a:.8f}x + {hex_3pt_b:.8f}y + {hex_3pt_c:.8f}z = {hex_3pt_d:.8f}")
print("=" * 60)

# =====================================================
# SKETCH POINTS - ORIGINAL THROUGH CUT (FIRST FEATURE)
# =====================================================
original_sketch_pts_3d = [
    (17.00, 35.13, 9.23),
    (16.82, 35.64, 9.22),
    (16.50, 36.13, 9.21),
    (16.06, 36.45, 9.21),
    (15.40, 36.63, 9.21),
    (14.72, 36.49, 9.21),
    (14.17, 36.18, 9.21),
    (13.89, 35.85, 9.22),
    (13.68, 35.44, 9.22),
    (13.62, 35.11, 9.23),
    (13.59, 34.85, 9.23),
    (13.59, 14.93, 9.53),
    (13.64, 14.47, 9.54),
    (13.77, 14.17, 9.54),
    (13.92, 13.91, 8.55),
    (14.16, 13.64, 8.55),
    (14.42, 13.45, 8.55),
    (14.75, 13.30, 8.56),
    (15.10, 13.23, 8.56),
    (15.40, 13.23, 8.56),
    (15.71, 13.26, 8.56),
    (16.01, 13.39, 8.55),
    (16.34, 13.58, 8.55),
    (16.72, 14.01, 8.55),
    (16.93, 14.50, 8.54),
    (16.97, 14.87, 8.53),
    (17.00, 15.13, 8.53),
]

original_sketch_z_plane = np.mean([p[2] for p in original_sketch_pts_3d])
original_sketch_pts_2d = [(p[0], p[1]) for p in original_sketch_pts_3d]

print("\n" + "=" * 60)
print("ORIGINAL SKETCH PROFILE - THROUGH CUT #1")
print("=" * 60)
print(f"Number of points: {len(original_sketch_pts_2d)}")
print(f"Sketch plane Z: {original_sketch_z_plane:.2f} mm")
print(f"Closed boundary: YES")
print("=" * 60)

# =====================================================
# NEW SKETCH POINTS - SECOND THROUGH CUT (NEW FEATURE)
# CLOSED BOUNDARY - 28 POINTS
# Z ADJUSTED: Top arc raised by +1.0mm
# =====================================================
new_sketch_pts_3d = [
    (13.58, 65.81, 8.77),
    (13.63, 66.16, 8.76),
    (13.71, 66.47, 8.76),
    (13.86, 66.78, 8.75),
    (14.04, 67.02, 8.75),
    (14.32, 67.28, 8.75),
    (14.70, 67.47, 8.74),
    (15.17, 67.57, 8.74),
    (15.60, 67.57, 8.74),
    (16.00, 67.42, 8.74),
    (16.30, 67.22, 8.75),
    (16.60, 66.92, 8.75),
    (16.85, 66.50, 8.76),
    (16.96, 66.18, 8.76),
    (16.97, 65.81, 8.77),
    (17.00, 46.03, 8.07),
    (16.93, 45.46, 8.07),
    (16.68, 44.95, 8.08),
    (16.42, 44.64, 8.09),
    (16.01, 44.38, 8.09),
    (15.45, 44.23, 8.09),
    (14.92, 44.25, 8.09),
    (14.53, 44.38, 8.09),
    (14.13, 44.66, 8.09),
    (13.82, 45.05, 8.08),
    (13.63, 45.47, 8.07),
    (13.59, 45.93, 8.07),
    (13.59, 46.06, 8.06),
]

new_sketch_z_plane = np.mean([p[2] for p in new_sketch_pts_3d])
new_sketch_pts_2d = [(p[0], p[1]) for p in new_sketch_pts_3d]

print("\n" + "=" * 60)
print("NEW SKETCH PROFILE - THROUGH CUT #2 (CLOSED BOUNDARY)")
print("=" * 60)
print(f"Number of points: {len(new_sketch_pts_2d)}")
print(f"Sketch plane Z: {new_sketch_z_plane:.2f} mm")
print(f"Closed boundary: YES")
print(f"Average Z value: {new_sketch_z_plane:.4f} mm")
print("=" * 60)

# =====================================================
# MIRRORED SKETCH POINTS #1 - YZ PLANE MIRROR
# Original Through Cut mirrored (X → -X)
# =====================================================
mirrored_original_sketch_pts_3d = [
    (-p[0], p[1], p[2]) for p in original_sketch_pts_3d
]

mirrored_original_sketch_z_plane = np.mean([p[2] for p in mirrored_original_sketch_pts_3d])
mirrored_original_sketch_pts_2d = [(p[0], p[1]) for p in mirrored_original_sketch_pts_3d]

print("\n" + "=" * 60)
print("MIRRORED SKETCH PROFILE #1 - YZ PLANE MIRROR")
print("=" * 60)
print(f"Number of points: {len(mirrored_original_sketch_pts_2d)}")
print(f"Sketch plane Z: {mirrored_original_sketch_z_plane:.2f} mm")
print(f"Mirror type: YZ Plane (X → -X)")
print(f"X Range: {min([p[0] for p in mirrored_original_sketch_pts_3d]):.2f} to {max([p[0] for p in mirrored_original_sketch_pts_3d]):.2f} mm")
print("=" * 60)

# =====================================================
# MIRRORED SKETCH POINTS #2 - YZ PLANE MIRROR
# New Through Cut mirrored (X → -X)
# =====================================================
mirrored_new_sketch_pts_3d = [
    (-p[0], p[1], p[2]) for p in new_sketch_pts_3d
]

mirrored_new_sketch_z_plane = np.mean([p[2] for p in mirrored_new_sketch_pts_3d])
mirrored_new_sketch_pts_2d = [(p[0], p[1]) for p in mirrored_new_sketch_pts_3d]

print("\n" + "=" * 60)
print("MIRRORED SKETCH PROFILE #2 - YZ PLANE MIRROR")
print("=" * 60)
print(f"Number of points: {len(mirrored_new_sketch_pts_2d)}")
print(f"Sketch plane Z: {mirrored_new_sketch_z_plane:.2f} mm")
print(f"Mirror type: YZ Plane (X → -X)")
print(f"X Range: {min([p[0] for p in mirrored_new_sketch_pts_3d]):.2f} to {max([p[0] for p in mirrored_new_sketch_pts_3d]):.2f} mm")
print("=" * 60)


# =====================================================
# THIRD SKETCH POINTS - PROFILE #5 (34-POINT CLOSED BOUNDARY)
# NEW THROUGH CUT FEATURE
# =====================================================
third_sketch_pts_3d = [
    (11.25, 45.35, 8.08),
    (11.32, 34.58, 8.24),
    (11.20, 31.03, 8.29),
    (10.32, 27.54, 8.34),
    (8.24, 24.18, 8.39),
    (6.55, 22.72, 8.41),
    (4.58, 21.60, 8.43),
    (2.53, 20.81, 8.44),
    (0.17, 20.50, 8.45),
    (-2.08, 20.69, 8.44),
    (-4.27, 21.30, 8.44),
    (-6.00, 22.13, 8.42),
    (-7.68, 23.30, 8.41),
    (-9.00, 24.63, 8.39),
    (-10.23, 26.46, 8.36),
    (-11.10, 28.53, 8.33),
    (-11.50, 30.13, 8.30),
    (-11.66, 32.11, 8.27),
    (-11.66, 34.58, 8.24),
    (-11.66, 48.13, 8.03),
    (-11.66, 49.13, 8.02),
    (-11.59, 50.51, 8.00),
    (-11.22, 52.22, 8.97),
    (-10.53, 54.09, 8.94),
    (-9.51, 55.68, 8.92),
    (-8.00, 57.12, 8.90),
    (-5.75, 58.91, 8.87),
    (-3.73, 59.84, 8.86),
    (-1.60, 60.34, 8.85),
    (0.52, 60.34, 8.85),
    (2.41, 60.08, 8.85),
    (4.52, 59.35, 8.87),
    (6.72, 58.06, 8.88),
    (8.42, 56.46, 8.91),
    (10.00, 54.28, 8.94),
]

third_sketch_z_plane = np.mean([p[2] for p in third_sketch_pts_3d])
third_sketch_pts_2d = [(p[0], p[1]) for p in third_sketch_pts_3d]

print("\n" + "=" * 60)
print("THIRD SKETCH PROFILE - THROUGH CUT #5")
print("=" * 60)
print(f"Number of points: {len(third_sketch_pts_2d)}")
print(f"Sketch plane Z: {third_sketch_z_plane:.2f} mm")
print(f"Closed boundary: YES")
print(f"X Range: {min([p[0] for p in third_sketch_pts_3d]):.2f} to {max([p[0] for p in third_sketch_pts_3d]):.2f} mm")
print(f"Y Range: {min([p[1] for p in third_sketch_pts_3d]):.2f} to {max([p[1] for p in third_sketch_pts_3d]):.2f} mm")
print("=" * 60)

# =====================================================
# MIRRORED SKETCH POINTS #3 - YZ PLANE MIRROR
# Third sketch profile mirrored (X → -X)
# =====================================================
mirrored_third_sketch_pts_3d = [
    (-p[0], p[1], p[2]) for p in third_sketch_pts_3d
]

mirrored_third_sketch_z_plane = np.mean([p[2] for p in mirrored_third_sketch_pts_3d])
mirrored_third_sketch_pts_2d = [(p[0], p[1]) for p in mirrored_third_sketch_pts_3d]

print("\n" + "=" * 60)
print("MIRRORED SKETCH PROFILE #3 - YZ PLANE MIRROR")
print("=" * 60)
print(f"Number of points: {len(mirrored_third_sketch_pts_2d)}")
print(f"Sketch plane Z: {mirrored_third_sketch_z_plane:.2f} mm")
print(f"Mirror type: YZ Plane (X → -X)")
print(f"X Range: {min([p[0] for p in mirrored_third_sketch_pts_3d]):.2f} to {max([p[0] for p in mirrored_third_sketch_pts_3d]):.2f} mm")
print("=" * 60)

# =====================================================
# RIGHT FACE PROFILE (YZ plane at X=90)
# =====================================================
profile_pts = [
    (-15.65, -19.22),
    (-15.65, -5.50),
    (-12.02, -1.88),
    (2.59, -1.89),
    (10.12, 5.64),
    (10.12, 7.05),
    (1.17, 16.00),
    (-2.03, 19.19),
    (-7.56, 19.19),
    (-23.85, 2.82),
    (-28.86, 2.79),
    (-28.86, -19.22),
]

# =====================================================
# NEW EXTRUSION PROFILE (XY plane at Z=16.06) - 12 POINTS
# =====================================================
new_extrude_pts = [
    (-33.26, 71.55),
    (-43.27, 61.33),
    (-43.27, 27.83),
    (-22.79, 27.83),
    (-22.79, 9.46),
    (22.33, 9.46),
    (22.33, 26.82),
    (24.67, 28.88),
    (41.32, 28.88),
    (43.23, 26.87),
    (43.23, 61.33),
    (33.40, 71.55),
]

# =====================================================
# NEW CUT PROFILE - 4 POINTS (SLIGHTLY TILTED PLANE)
# Top edge at Y=71.55, Z=17.68
# Bottom edge at Y=71.40, Z=7.67
# Use custom plane calculated from 4 points
# =====================================================
new_cut_pts_3d = [
    (22.33, 72.55, 17.68),    # Top Right
    (-22.79, 72.55, 17.68),   # Top Left
    (-22.61, 72.40, 7.67),    # Bottom Left
    (22.39, 72.40, 7.67),     # Bottom Right
]

# =====================================================
# BUILD PART
# =====================================================
with BuildPart() as new_part:

    # =================================================
    # RIGHT FACE PROFILE - EXTRUDE 176mm
    # =================================================
    right_face_plane = Plane.YZ.offset(90.00)

    with BuildSketch(right_face_plane):
        Polygon(*profile_pts)

    extrude(amount=-180)

    # =================================================
    # TOP FACE PROFILE - EXTRUDE 17.959mm
    # =================================================
    top_face_pts = [
        (43.25, 1.10),
        (22.33, 1.10),
        (22.33, 26.82),
        (24.33, 28.82),
        (41.25, 28.82),
        (43.25, 26.82),
    ]

    top_face_plane = Plane.XY.offset(16.06)

    with BuildSketch(top_face_plane):
        Polygon(*top_face_pts)

    extrude(amount=-17.959)

    # =================================================
    # XZ PLANE PROFILE - EXTRUDE 27.721mm
    # =================================================
    xz_plane_pts = [
        (-22.77, -1.73),
        (-43.26, -1.82),
        (-43.35, 6.97),
        (-34.30, 16.06),
        (-22.68, 16.09),
    ]

    xz_plane = Plane.XZ.offset(0)

    with BuildSketch(xz_plane):
        Polygon(*xz_plane_pts)

    extrude(amount=-27.721)

    # =================================================
    # NEW BOUNDARY PROFILE - 3 POINT CLOSED BOUNDARY - EXTRUDE 5MM
    # FRONT FACE (XZ PLANE) - Y values are nearly constant (~27.72)
    # Sketch Points: X: -43.35 Y: 27.72 Z: 6.97 mm
    #               X: -43.27 Y: 27.83 Z: 16.06 mm
    #               X: -34.30 Y: 27.72 Z: 16.06 mm
    # =================================================
    boundary_sketch_pts_3d = [
        (-43.35, -23, 6.97),
        (-43.27, -23, 16.06),
        (-34.30, -23, 16.06),
    ]
    
    # Profile is on FRONT FACE (XZ plane) - use average Y as offset
    boundary_sketch_y_plane = np.mean([p[1] for p in boundary_sketch_pts_3d])
    # 2D coordinates on XZ plane: (X, Z)
    boundary_sketch_pts_2d = [(p[0], p[2]) for p in boundary_sketch_pts_3d]
    
    print("\n" + "=" * 60)
    print("BOUNDARY PROFILE - CLOSED 3-POINT SKETCH (FRONT FACE)")
    print("=" * 60)
    print(f"Number of points: {len(boundary_sketch_pts_2d)}")
    print(f"Sketch plane Y (XZ offset): {boundary_sketch_y_plane:.2f} mm")
    print(f"2D Points (X,Z): {boundary_sketch_pts_2d}")
    print("=" * 60)
    
    # XZ plane at Y = 27.76 (front face position)
    boundary_sketch_plane = Plane.XZ.offset(boundary_sketch_y_plane)
    
    try:
        with BuildSketch(boundary_sketch_plane):
            Polygon(*boundary_sketch_pts_2d)
        
        # Extrude 5mm in -Y direction (into the part / backwards)
        extrude(amount=-5)
        print(f"\n✓ Boundary profile extrusion created successfully")
        print(f"  Points: {len(boundary_sketch_pts_2d)}")
        print(f"  Sketch Plane Y: {boundary_sketch_y_plane:.2f} mm (XZ plane)")
        print(f"  Extrusion depth: 5 mm (in -Y direction)")
        
    except Exception as e:
        print(f"\n⚠ Boundary profile extrusion failed: {e}")
        print("  Attempting with reversed polygon winding...")
        try:
            boundary_sketch_pts_2d_reversed = list(reversed(boundary_sketch_pts_2d))
            with BuildSketch(boundary_sketch_plane):
                Polygon(*boundary_sketch_pts_2d_reversed)
            extrude(amount=-5)
            print("✓ Boundary profile created with reversed winding")
        except Exception as e2:
            print(f"⚠ Reversed also failed: {e2}")
            print("  Trying +5mm direction...")
            try:
                with BuildSketch(boundary_sketch_plane):
                    Polygon(*boundary_sketch_pts_2d)
                extrude(amount=5)
                print("✓ Boundary profile created with +5mm direction")
            except Exception as e3:
                print(f"✗ All attempts failed: {e3}")

    # =================================================
    # NEW: EXTRUSION FROM 12 POINTS - FLIPPED to -18mm
    # XY Plane at Z = 16.06 (TOP FACE)
    # =================================================
    new_extrude_plane = Plane.XY.offset(16.06)

    with BuildSketch(new_extrude_plane):
        Polygon(*new_extrude_pts)

    extrude(amount=-18)   # FLIPPED FROM +18 TO -18
    print("\n✓ New extrusion created (FLIPPED: -18mm direction)")

    # =================================================
    # NEW CUT: EXTRUDE CUT 70MM FROM 4 POINTS
    # CUSTOM TILTED PLANE (Y=71.55 top, Y=71.40 bottom)
    # =================================================
    # Calculate custom plane from the 4 points
    cut_pts_arr = np.array(new_cut_pts_3d)
    cut_origin = cut_pts_arr.mean(axis=0)
    
    # X direction along top edge (P2 - P1)
    cut_x_dir = cut_pts_arr[1] - cut_pts_arr[0]
    cut_x_dir = cut_x_dir / np.linalg.norm(cut_x_dir)
    
    # Side vector (P4 - P1) - going down-front
    cut_side = cut_pts_arr[3] - cut_pts_arr[0]
    
    # Normal = X × side
    cut_normal = np.cross(cut_x_dir, cut_side)
    cut_normal = cut_normal / np.linalg.norm(cut_normal)
    
    # Y direction in-plane = normal × X
    cut_y_dir = np.cross(cut_normal, cut_x_dir)
    cut_y_dir = cut_y_dir / np.linalg.norm(cut_y_dir)
    
    # Project 4 points to 2D coords on the custom plane
    cut_pts_2d = []
    for p in cut_pts_arr:
        rel = p - cut_origin
        x_coord = float(np.dot(rel, cut_x_dir))
        y_coord = float(np.dot(rel, cut_y_dir))
        cut_pts_2d.append((x_coord, y_coord))
    
    print(f"\nCut Plane Origin: {cut_origin}")
    print(f"Cut Plane Normal: {cut_normal}")
    print(f"Projected 2D Points: {cut_pts_2d}")
    
    try:
        # Create custom plane
        cut_plane_custom = Plane(
            origin=Vector(float(cut_origin[0]), float(cut_origin[1]), float(cut_origin[2])),
            x_dir=Vector(float(cut_x_dir[0]), float(cut_x_dir[1]), float(cut_x_dir[2])),
            y_dir=Vector(float(cut_y_dir[0]), float(cut_y_dir[1]), float(cut_y_dir[2]))
        )
        
        with BuildSketch(cut_plane_custom):
            Polygon(*cut_pts_2d)
        
        # Extrude cut 70mm in -normal direction (into the part)
        extrude(amount=70, mode=Mode.SUBTRACT)
        print("✓ New CUT created (70mm) - Custom tilted plane")
        
    except Exception as e:
        print(f"⚠ Custom plane cut failed: {e}")
        print("  Trying with positive direction...")
        try:
            with BuildSketch(cut_plane_custom):
                Polygon(*cut_pts_2d)
            extrude(amount=-75, mode=Mode.SUBTRACT)
            print("✓ CUT created with +70mm direction")
        except Exception as e2:
            print(f"✗ Both directions failed: {e2}")

    # =================================================
    # SKETCH PROFILE #1 - ORIGINAL THROUGH CUT (CLOSED BOUNDARY)
    # 27-POINT CLOSED PROFILE
    # =================================================
    original_sketch_plane = Plane.XY.offset(original_sketch_z_plane)
    
    try:
        with BuildSketch(original_sketch_plane):
            Polygon(*original_sketch_pts_2d)
        
        # Create through cut (extrude deep into part to ensure complete cut)
        extrude(amount=-300, mode=Mode.SUBTRACT)
        print(f"\n✓ ORIGINAL sketch profile through cut #1 created successfully")
        print(f"  Points: {len(original_sketch_pts_2d)}")
        print(f"  Sketch Plane Z: {original_sketch_z_plane:.2f} mm")
        print(f"  Cut depth: 300 mm (through)")
        
    except Exception as e:
        print(f"\n⚠ Original sketch profile cut failed: {e}")
        print("  Attempting with reversed polygon winding...")
        try:
            # Reverse point order in case of winding direction issue
            original_sketch_pts_2d_reversed = list(reversed(original_sketch_pts_2d))
            with BuildSketch(original_sketch_plane):
                Polygon(*original_sketch_pts_2d_reversed)
            extrude(amount=300, mode=Mode.SUBTRACT)
            print("✓ Original sketch profile cut created with reversed winding")
        except Exception as e2:
            print(f"✗ Original cut reversed attempt also failed: {e2}")

    # =================================================
    # SKETCH PROFILE #2 - NEW THROUGH CUT (CLOSED BOUNDARY)
    # 28-POINT CLOSED PROFILE
    # =================================================
    new_sketch_plane = Plane.XY.offset(new_sketch_z_plane)
    
    try:
        with BuildSketch(new_sketch_plane):
            Polygon(*new_sketch_pts_2d)
        
        # Create through cut (extrude deep into part to ensure complete cut)
        extrude(amount=-300, mode=Mode.SUBTRACT)
        print(f"\n✓ NEW sketch profile through cut #2 created successfully")
        print(f"  Points: {len(new_sketch_pts_2d)}")
        print(f"  Sketch Plane Z: {new_sketch_z_plane:.2f} mm")
        print(f"  Cut depth: 300 mm (through)")
        
    except Exception as e:
        print(f"\n⚠ New sketch profile cut failed: {e}")
        print("  Attempting with reversed polygon winding...")
        try:
            # Reverse point order in case of winding direction issue
            new_sketch_pts_2d_reversed = list(reversed(new_sketch_pts_2d))
            with BuildSketch(new_sketch_plane):
                Polygon(*new_sketch_pts_2d_reversed)
            extrude(amount=300, mode=Mode.SUBTRACT)
            print("✓ New sketch profile cut created with reversed winding")
        except Exception as e2:
            print(f"✗ New cut reversed attempt also failed: {e2}")

    # =================================================
    # SKETCH PROFILE #3 - MIRRORED CUT #1 (YZ PLANE MIRROR)
    # 27-POINT CLOSED PROFILE (X → -X)
    # =================================================
    mirrored_original_sketch_plane = Plane.XY.offset(mirrored_original_sketch_z_plane)
    
    try:
        with BuildSketch(mirrored_original_sketch_plane):
            Polygon(*mirrored_original_sketch_pts_2d)
        
        # Create through cut (extrude deep into part to ensure complete cut)
        extrude(amount=-300, mode=Mode.SUBTRACT)
        print(f"\n✓ MIRRORED sketch profile through cut #3 created successfully")
        print(f"  Points: {len(mirrored_original_sketch_pts_2d)}")
        print(f"  Sketch Plane Z: {mirrored_original_sketch_z_plane:.2f} mm")
        print(f"  Mirror: YZ Plane (negative X side)")
        print(f"  Cut depth: 300 mm (through)")
        
    except Exception as e:
        print(f"\n⚠ Mirrored sketch profile #1 cut failed: {e}")
        print("  Attempting with reversed polygon winding...")
        try:
            # Reverse point order in case of winding direction issue
            mirrored_original_sketch_pts_2d_reversed = list(reversed(mirrored_original_sketch_pts_2d))
            with BuildSketch(mirrored_original_sketch_plane):
                Polygon(*mirrored_original_sketch_pts_2d_reversed)
            extrude(amount=300, mode=Mode.SUBTRACT)
            print("✓ Mirrored sketch profile #1 cut created with reversed winding")
        except Exception as e2:
            print(f"✗ Mirrored cut #1 reversed attempt also failed: {e2}")

    # =================================================
    # SKETCH PROFILE #4 - MIRRORED CUT #2 (YZ PLANE MIRROR)
    # 28-POINT CLOSED PROFILE (X → -X)
    # =================================================
    mirrored_new_sketch_plane = Plane.XY.offset(mirrored_new_sketch_z_plane)
    
    try:
        with BuildSketch(mirrored_new_sketch_plane):
            Polygon(*mirrored_new_sketch_pts_2d)
        
        # Create through cut (extrude deep into part to ensure complete cut)
        extrude(amount=-300, mode=Mode.SUBTRACT)
        print(f"\n✓ MIRRORED sketch profile through cut #4 created successfully")
        print(f"  Points: {len(mirrored_new_sketch_pts_2d)}")
        print(f"  Sketch Plane Z: {mirrored_new_sketch_z_plane:.2f} mm")
        print(f"  Mirror: YZ Plane (negative X side)")
        print(f"  Cut depth: 300 mm (through)")
        
    except Exception as e:
        print(f"\n⚠ Mirrored sketch profile #2 cut failed: {e}")
        print("  Attempting with reversed polygon winding...")
        try:
            # Reverse point order in case of winding direction issue
            mirrored_new_sketch_pts_2d_reversed = list(reversed(mirrored_new_sketch_pts_2d))
            with BuildSketch(mirrored_new_sketch_plane):
                Polygon(*mirrored_new_sketch_pts_2d_reversed)
            extrude(amount=300, mode=Mode.SUBTRACT)
            print("✓ Mirrored sketch profile #2 cut created with reversed winding")
        except Exception as e2:
            print(f"✗ Mirrored cut #2 reversed attempt also failed: {e2}")


    # =================================================
    # SKETCH PROFILE #5 - THIRD THROUGH CUT (CLOSED BOUNDARY)
    # 34-POINT CLOSED PROFILE
    # =================================================
    third_sketch_plane = Plane.XY.offset(third_sketch_z_plane)
    
    try:
        with BuildSketch(third_sketch_plane):
            Polygon(*third_sketch_pts_2d)
        
        # Create through cut (extrude deep into part to ensure complete cut)
        extrude(amount=-300, mode=Mode.SUBTRACT)
        print(f"\n✓ THIRD sketch profile through cut #5 created successfully")
        print(f"  Points: {len(third_sketch_pts_2d)}")
        print(f"  Sketch Plane Z: {third_sketch_z_plane:.2f} mm")
        print(f"  Cut depth: 300 mm (through)")
        
    except Exception as e:
        print(f"\n⚠ Third sketch profile cut failed: {e}")
        print("  Attempting with reversed polygon winding...")
        try:
            # Reverse point order in case of winding direction issue
            third_sketch_pts_2d_reversed = list(reversed(third_sketch_pts_2d))
            with BuildSketch(third_sketch_plane):
                Polygon(*third_sketch_pts_2d_reversed)
            extrude(amount=300, mode=Mode.SUBTRACT)
            print("✓ Third sketch profile cut created with reversed winding")
        except Exception as e2:
            print(f"✗ Third cut reversed attempt also failed: {e2}")

    # =================================================
    # SKETCH PROFILE #6 - MIRRORED CUT #3 (YZ PLANE MIRROR)
    # 34-POINT CLOSED PROFILE (X → -X)
    # =================================================
    mirrored_third_sketch_plane = Plane.XY.offset(mirrored_third_sketch_z_plane)
    
    try:
        with BuildSketch(mirrored_third_sketch_plane):
            Polygon(*mirrored_third_sketch_pts_2d)
        
        # Create through cut (extrude deep into part to ensure complete cut)
        extrude(amount=-300, mode=Mode.SUBTRACT)
        print(f"\n✓ MIRRORED sketch profile through cut #6 created successfully")
        print(f"  Points: {len(mirrored_third_sketch_pts_2d)}")
        print(f"  Sketch Plane Z: {mirrored_third_sketch_z_plane:.2f} mm")
        print(f"  Mirror: YZ Plane (negative X side)")
        print(f"  Cut depth: 300 mm (through)")
        
    except Exception as e:
        print(f"\n⚠ Mirrored sketch profile #3 cut failed: {e}")
        print("  Attempting with reversed polygon winding...")
        try:
            # Reverse point order in case of winding direction issue
            mirrored_third_sketch_pts_2d_reversed = list(reversed(mirrored_third_sketch_pts_2d))
            with BuildSketch(mirrored_third_sketch_plane):
                Polygon(*mirrored_third_sketch_pts_2d_reversed)
            extrude(amount=300, mode=Mode.SUBTRACT)
            print("✓ Mirrored sketch profile #3 cut created with reversed winding")
        except Exception as e2:
            print(f"✗ Mirrored cut #3 reversed attempt also failed: {e2}")

    # =================================================
    # NEW: HEXAGON CUTS ON SVD PLANE (3-POINT)
    # Circumscribed diameter: 13.5mm (radius: 6.75mm)
    # Extrude cut depth: 40mm
    # Positions: (75.00, -0.01, 9.89) and (-50.00, -0.01, 9.89)
    # =================================================
    
    # Create hexagon with circumscribed radius 6.75mm
    hex_circumradius = 6.75  # Half of 13.5mm diameter
    hex_angles_3pt = np.linspace(0, 2 * np.pi, 7)[:-1]
    hex_vertices_3pt = [(hex_circumradius * np.cos(angle), hex_circumradius * np.sin(angle)) 
                         for angle in hex_angles_3pt]
    
    # Calculate plane vectors for the SVD plane
    hex_3pt_normal_vec = hex_3pt_normal
    
    # Find perpendicular vectors to the normal
    if abs(hex_3pt_c) < 0.9:
        hex_3pt_x_dir_temp = np.array([hex_3pt_c, 0, -hex_3pt_a])
    else:
        hex_3pt_x_dir_temp = np.array([0, hex_3pt_c, -hex_3pt_b])
    
    hex_3pt_x_dir_normalized = hex_3pt_x_dir_temp / np.linalg.norm(hex_3pt_x_dir_temp)
    hex_3pt_y_dir_normalized = np.cross(hex_3pt_normal_vec, hex_3pt_x_dir_normalized)
    hex_3pt_y_dir_normalized = hex_3pt_y_dir_normalized / np.linalg.norm(hex_3pt_y_dir_normalized)
    
    # Hexagon cut positions on the plane
    hexagon_3pt_cut_positions = [
        (75.00, -0.01, 9.89),      # Position 1
        (-50.00, -0.01, 9.89),     # Position 2
    ]
    
    print("\n" + "=" * 60)
    print("HEXAGON CUTS ON SVD PLANE (3-POINT CALCULATION)")
    print("=" * 60)
    print(f"Hexagon Circumscribed Diameter: 13.5 mm (Radius: {hex_circumradius} mm)")
    print(f"Extrude Cut Depth: 40 mm")
    print(f"SVD Plane Normal: [{hex_3pt_a:.8f}, {hex_3pt_b:.8f}, {hex_3pt_c:.8f}]")
    print(f"Position 1: (75.00, -0.01, 9.89)")
    print(f"Position 2: (-50.00, -0.01, 9.89)")
    print("=" * 60)
    
    try:
        hex_3pt_plane_custom = Plane(
            origin=Vector(float(hex_3pt_pt1[0]), float(hex_3pt_pt1[1]), float(hex_3pt_pt1[2])),
            x_dir=Vector(float(hex_3pt_x_dir_normalized[0]), float(hex_3pt_x_dir_normalized[1]), float(hex_3pt_x_dir_normalized[2])),
            y_dir=Vector(float(hex_3pt_y_dir_normalized[0]), float(hex_3pt_y_dir_normalized[1]), float(hex_3pt_y_dir_normalized[2]))
        )
        
        # Project cut positions onto the 2D plane
        hex_3pt_cut_pts_2d = []
        for pt_3d in hexagon_3pt_cut_positions:
            pt_arr = np.array(pt_3d)
            rel = pt_arr - hex_3pt_pt1
            x_coord = float(np.dot(rel, hex_3pt_x_dir_normalized))
            y_coord = float(np.dot(rel, hex_3pt_y_dir_normalized))
            hex_3pt_cut_pts_2d.append((x_coord, y_coord))
        
        with BuildSketch(hex_3pt_plane_custom):
            for pos in hex_3pt_cut_pts_2d:
                with Locations(pos):
                    Polygon(*hex_vertices_3pt)
        
        extrude(amount=-28, mode=Mode.SUBTRACT)
        print("\n✓ Hexagon SVD plane cuts (3-point) created successfully")
        print(f"  Number of hexagons: 2")
        print(f"  Extrude depth: 40 mm")
        print(f"  Hexagon vertices (6): {len(hex_vertices_3pt)}")
        
    except Exception as e:
        print(f"\n⚠ Hexagon 3-point cuts failed: {e}")
        print("  Attempting with reversed winding...")
        try:
            hex_vertices_3pt_reversed = list(reversed(hex_vertices_3pt))
            with BuildSketch(hex_3pt_plane_custom):
                for pos in hex_3pt_cut_pts_2d:
                    with Locations(pos):
                        Polygon(*hex_vertices_3pt_reversed)
            extrude(amount=40, mode=Mode.SUBTRACT)
            print("✓ Hexagon cuts created with reversed winding")
        except Exception as e2:
            print(f"⚠ Reversed also failed: {e2}")
            print("  Trying with -40mm direction...")
            try:
                with BuildSketch(hex_3pt_plane_custom):
                    for pos in hex_3pt_cut_pts_2d:
                        with Locations(pos):
                            Polygon(*hex_vertices_3pt)
                extrude(amount=-40, mode=Mode.SUBTRACT)
                print("✓ Hexagon cuts created with -40mm direction")
            except Exception as e3:
                print(f"✗ All attempts failed: {e3}")
    
    # =================================================
    # 8MM DIAMETER THROUGH HOLE - AXIS THROUGH TWO POINTS
    # Point 1: X: 51.22, Y: -22.71, Z: 3.97 mm
    # Point 2: X: 51.22, Y: -19.14, Z: 0.42 mm
    # =================================================
    pt1_custom = np.array([51.22, -32.114, 13.33])
    pt2_custom = np.array([51.22, -19.14, 0.42])
    
    # Midpoint (hole center)
    hole_midpoint = (pt1_custom + pt2_custom) / 2
    
    # Hole axis direction
    hole_axis = pt2_custom - pt1_custom
    hole_axis = hole_axis / np.linalg.norm(hole_axis)
    
    # Create perpendicular axes for the plane
    # Find a vector perpendicular to hole_axis
    if abs(hole_axis[0]) < 0.9:
        perp_temp = np.array([1, 0, 0])
    else:
        perp_temp = np.array([0, 1, 0])
    
    hole_x_dir = np.cross(hole_axis, perp_temp)
    hole_x_dir = hole_x_dir / np.linalg.norm(hole_x_dir)
    
    hole_y_dir = np.cross(hole_axis, hole_x_dir)
    hole_y_dir = hole_y_dir / np.linalg.norm(hole_y_dir)
    
    print(f"\n" + "=" * 60)
    print("8MM THROUGH HOLE (AXIS THROUGH TWO POINTS)")
    print("=" * 60)
    print(f"Point 1: {pt1_custom}")
    print(f"Point 2: {pt2_custom}")
    print(f"Midpoint: {hole_midpoint}")
    print(f"Hole Axis: {hole_axis}")
    print(f"Hole Axis Length: {np.linalg.norm(pt2_custom - pt1_custom):.4f} mm")
    print("=" * 60)
    
    try:
        custom_hole_plane = Plane(
            origin=Vector(float(hole_midpoint[0]), float(hole_midpoint[1]), float(hole_midpoint[2])),
            x_dir=Vector(float(hole_x_dir[0]), float(hole_x_dir[1]), float(hole_x_dir[2])),
            y_dir=Vector(float(hole_y_dir[0]), float(hole_y_dir[1]), float(hole_y_dir[2]))
        )
        
        with BuildSketch(custom_hole_plane):
            Circle(4.0)  # 8mm diameter (radius = 4mm)
        
        extrude(amount=500, mode=Mode.SUBTRACT)
        print("✓ 8mm through hole created successfully")
        print(f"  Hole center: X={hole_midpoint[0]:.2f}, Y={hole_midpoint[1]:.2f}, Z={hole_midpoint[2]:.2f}")
        
    except Exception as e:
        print(f"⚠ Custom hole plane failed: {e}")
        print("  Attempting fallback...")
        try:
            # Fallback: Simple hole at midpoint on XY plane
            fallback_plane = Plane.XY.offset(float(hole_midpoint[2]))
            with BuildSketch(fallback_plane):
                with Locations((float(hole_midpoint[0]), float(hole_midpoint[1]))):
                    Circle(4.0)
            extrude(amount=-500, mode=Mode.SUBTRACT)
            print("✓ Hole created using fallback XY plane")
        except Exception as e2:
            print(f"✗ Fallback also failed: {e2}")

    # =================================================
    # SECOND 8MM DIAMETER THROUGH HOLE - AXIS THROUGH TWO POINTS
    # Point 1: X: -79.79, Y: -22.71, Z: 3.97 mm
    # Point 2: X: -79.79, Y: -19.14, Z: 0.42 mm
    # =================================================
    pt1_custom_2 = np.array([-79.79, -32.11, 13.33])
    pt2_custom_2 = np.array([-79.79, -19.14, 0.42])
    
    # Midpoint (hole center)
    hole_midpoint_2 = (pt1_custom_2 + pt2_custom_2) / 2
    
    # Hole axis direction
    hole_axis_2 = pt2_custom_2 - pt1_custom_2
    hole_axis_2 = hole_axis_2 / np.linalg.norm(hole_axis_2)
    
    # Create perpendicular axes for the plane
    # Find a vector perpendicular to hole_axis
    if abs(hole_axis_2[0]) < 0.9:
        perp_temp_2 = np.array([1, 0, 0])
    else:
        perp_temp_2 = np.array([0, 1, 0])
    
    hole_x_dir_2 = np.cross(hole_axis_2, perp_temp_2)
    hole_x_dir_2 = hole_x_dir_2 / np.linalg.norm(hole_x_dir_2)
    
    hole_y_dir_2 = np.cross(hole_axis_2, hole_x_dir_2)
    hole_y_dir_2 = hole_y_dir_2 / np.linalg.norm(hole_y_dir_2)
    
    print(f"\n" + "=" * 60)
    print("8MM THROUGH HOLE #2 (AXIS THROUGH TWO POINTS)")
    print("=" * 60)
    print(f"Point 1: {pt1_custom_2}")
    print(f"Point 2: {pt2_custom_2}")
    print(f"Midpoint: {hole_midpoint_2}")
    print(f"Hole Axis: {hole_axis_2}")
    print(f"Hole Axis Length: {np.linalg.norm(pt2_custom_2 - pt1_custom_2):.4f} mm")
    print("=" * 60)
    
    try:
        custom_hole_plane_2 = Plane(
            origin=Vector(float(hole_midpoint_2[0]), float(hole_midpoint_2[1]), float(hole_midpoint_2[2])),
            x_dir=Vector(float(hole_x_dir_2[0]), float(hole_x_dir_2[1]), float(hole_x_dir_2[2])),
            y_dir=Vector(float(hole_y_dir_2[0]), float(hole_y_dir_2[1]), float(hole_y_dir_2[2]))
        )
        
        with BuildSketch(custom_hole_plane_2):
            Circle(4.0)  # 8mm diameter (radius = 4mm)
        
        extrude(amount=500, mode=Mode.SUBTRACT)
        print("✓ 8mm through hole #2 created successfully")
        print(f"  Hole center: X={hole_midpoint_2[0]:.2f}, Y={hole_midpoint_2[1]:.2f}, Z={hole_midpoint_2[2]:.2f}")
        
    except Exception as e:
        print(f"⚠ Custom hole #2 plane failed: {e}")
        print("  Attempting fallback...")
        try:
            # Fallback: Simple hole at midpoint on XY plane
            fallback_plane_2 = Plane.XY.offset(float(hole_midpoint_2[2]))
            with BuildSketch(fallback_plane_2):
                with Locations((float(hole_midpoint_2[0]), float(hole_midpoint_2[1]))):
                    Circle(4.0)
            extrude(amount=-500, mode=Mode.SUBTRACT)
            print("✓ Hole #2 created using fallback XY plane")
        except Exception as e2:
            print(f"✗ Fallback #2 also failed: {e2}")

    # =================================================
    # 6MM DIAMETER THROUGH HOLE #1 - AXIS THROUGH TWO POINTS
    # Point 1: X: 74.67, Y: -36.34, Z: -25.32 mm
    # Point 2: X: 75.00, Y: 26.41, Z: 36.40 mm
    # =================================================
    pt1_6mm_hole1 = np.array([74.67, -36.34, -25.32])
    pt2_6mm_hole1 = np.array([75.00, 26.41, 36.40])
    
    # Midpoint (hole center)
    hole_midpoint_6mm_1 = (pt1_6mm_hole1 + pt2_6mm_hole1) / 2
    
    # Hole axis direction
    hole_axis_6mm_1 = pt2_6mm_hole1 - pt1_6mm_hole1
    hole_axis_6mm_1 = hole_axis_6mm_1 / np.linalg.norm(hole_axis_6mm_1)
    
    # Create perpendicular axes for the plane
    if abs(hole_axis_6mm_1[0]) < 0.9:
        perp_temp_6mm_1 = np.array([1, 0, 0])
    else:
        perp_temp_6mm_1 = np.array([0, 1, 0])
    
    hole_x_dir_6mm_1 = np.cross(hole_axis_6mm_1, perp_temp_6mm_1)
    hole_x_dir_6mm_1 = hole_x_dir_6mm_1 / np.linalg.norm(hole_x_dir_6mm_1)
    
    hole_y_dir_6mm_1 = np.cross(hole_axis_6mm_1, hole_x_dir_6mm_1)
    hole_y_dir_6mm_1 = hole_y_dir_6mm_1 / np.linalg.norm(hole_y_dir_6mm_1)
    
    print(f"\n" + "=" * 60)
    print("6MM THROUGH HOLE #1 (AXIS THROUGH TWO POINTS)")
    print("=" * 60)
    print(f"Point 1: {pt1_6mm_hole1}")
    print(f"Point 2: {pt2_6mm_hole1}")
    print(f"Midpoint: {hole_midpoint_6mm_1}")
    print(f"Hole Axis: {hole_axis_6mm_1}")
    print(f"Hole Axis Length: {np.linalg.norm(pt2_6mm_hole1 - pt1_6mm_hole1):.4f} mm")
    print("=" * 60)
    
    try:
        custom_hole_plane_6mm_1 = Plane(
            origin=Vector(float(hole_midpoint_6mm_1[0]), float(hole_midpoint_6mm_1[1]), float(hole_midpoint_6mm_1[2])),
            x_dir=Vector(float(hole_x_dir_6mm_1[0]), float(hole_x_dir_6mm_1[1]), float(hole_x_dir_6mm_1[2])),
            y_dir=Vector(float(hole_y_dir_6mm_1[0]), float(hole_y_dir_6mm_1[1]), float(hole_y_dir_6mm_1[2]))
        )
        
        with BuildSketch(custom_hole_plane_6mm_1):
            Circle(3.0)  # 6mm diameter (radius = 3mm)
        
        extrude(amount=500, mode=Mode.SUBTRACT)
        print("✓ 6mm through hole #1 created successfully")
        print(f"  Hole center: X={hole_midpoint_6mm_1[0]:.2f}, Y={hole_midpoint_6mm_1[1]:.2f}, Z={hole_midpoint_6mm_1[2]:.2f}")
        
    except Exception as e:
        print(f"⚠ Custom 6mm hole #1 plane failed: {e}")
        print("  Attempting fallback...")
        try:
            # Fallback: Simple hole at midpoint on XY plane
            fallback_plane_6mm_1 = Plane.XY.offset(float(hole_midpoint_6mm_1[2]))
            with BuildSketch(fallback_plane_6mm_1):
                with Locations((float(hole_midpoint_6mm_1[0]), float(hole_midpoint_6mm_1[1]))):
                    Circle(3.0)
            extrude(amount=-500, mode=Mode.SUBTRACT)
            print("✓ 6mm hole #1 created using fallback XY plane")
        except Exception as e2:
            print(f"✗ Fallback #1 also failed: {e2}")

    # =================================================
    # 6MM DIAMETER THROUGH HOLE #2 - AXIS THROUGH TWO POINTS
    # Point 1: X: -50.51, Y: -36.34, Z: -25.32 mm
    # Point 2: X: -50.00, Y: 26.41, Z: 36.40 mm
    # =================================================
    pt1_6mm_hole2 = np.array([-50.51, -36.34, -25.32])
    pt2_6mm_hole2 = np.array([-50.00, 26.41, 36.40])
    
    # Midpoint (hole center)
    hole_midpoint_6mm_2 = (pt1_6mm_hole2 + pt2_6mm_hole2) / 2
    
    # Hole axis direction
    hole_axis_6mm_2 = pt2_6mm_hole2 - pt1_6mm_hole2
    hole_axis_6mm_2 = hole_axis_6mm_2 / np.linalg.norm(hole_axis_6mm_2)
    
    # Create perpendicular axes for the plane
    if abs(hole_axis_6mm_2[0]) < 0.9:
        perp_temp_6mm_2 = np.array([1, 0, 0])
    else:
        perp_temp_6mm_2 = np.array([0, 1, 0])
    
    hole_x_dir_6mm_2 = np.cross(hole_axis_6mm_2, perp_temp_6mm_2)
    hole_x_dir_6mm_2 = hole_x_dir_6mm_2 / np.linalg.norm(hole_x_dir_6mm_2)
    
    hole_y_dir_6mm_2 = np.cross(hole_axis_6mm_2, hole_x_dir_6mm_2)
    hole_y_dir_6mm_2 = hole_y_dir_6mm_2 / np.linalg.norm(hole_y_dir_6mm_2)
    
    print(f"\n" + "=" * 60)
    print("6MM THROUGH HOLE #2 (AXIS THROUGH TWO POINTS)")
    print("=" * 60)
    print(f"Point 1: {pt1_6mm_hole2}")
    print(f"Point 2: {pt2_6mm_hole2}")
    print(f"Midpoint: {hole_midpoint_6mm_2}")
    print(f"Hole Axis: {hole_axis_6mm_2}")
    print(f"Hole Axis Length: {np.linalg.norm(pt2_6mm_hole2 - pt1_6mm_hole2):.4f} mm")
    print("=" * 60)
    
    try:
        custom_hole_plane_6mm_2 = Plane(
            origin=Vector(float(hole_midpoint_6mm_2[0]), float(hole_midpoint_6mm_2[1]), float(hole_midpoint_6mm_2[2])),
            x_dir=Vector(float(hole_x_dir_6mm_2[0]), float(hole_x_dir_6mm_2[1]), float(hole_x_dir_6mm_2[2])),
            y_dir=Vector(float(hole_y_dir_6mm_2[0]), float(hole_y_dir_6mm_2[1]), float(hole_y_dir_6mm_2[2]))
        )
        
        with BuildSketch(custom_hole_plane_6mm_2):
            Circle(3.0)  # 6mm diameter (radius = 3mm)
        
        extrude(amount=500, mode=Mode.SUBTRACT)
        print("✓ 6mm through hole #2 created successfully")
        print(f"  Hole center: X={hole_midpoint_6mm_2[0]:.2f}, Y={hole_midpoint_6mm_2[1]:.2f}, Z={hole_midpoint_6mm_2[2]:.2f}")
        
    except Exception as e:
        print(f"⚠ Custom 6mm hole #2 plane failed: {e}")
        print("  Attempting fallback...")
        try:
            # Fallback: Simple hole at midpoint on XY plane
            fallback_plane_6mm_2 = Plane.XY.offset(float(hole_midpoint_6mm_2[2]))
            with BuildSketch(fallback_plane_6mm_2):
                with Locations((float(hole_midpoint_6mm_2[0]), float(hole_midpoint_6mm_2[1]))):
                    Circle(3.0)
            extrude(amount=-500, mode=Mode.SUBTRACT)
            print("✓ 6mm hole #2 created using fallback XY plane")
        except Exception as e2:
            print(f"✗ Fallback #2 also failed: {e2}")

    # =================================================
    # 8MM DIAMETER THROUGH HOLES - BACK FACE
    # XZ Plane at Y = -15.59
    # =================================================
    hole_positions = [
        (65.00, -8.00),
        (-0.07, -8.19),
        (-64.98, -8.21),
    ]

    back_plane = Plane.XZ.offset(-15.59)

    with BuildSketch(back_plane):
        for pt in hole_positions:
            with Locations(pt):
                Circle(4.0)  # 8mm DIA (radius = 4mm)

    extrude(amount=400, mode=Mode.SUBTRACT)

    # =================================================
    # PROFILE CUT - EXTRUDE 38mm (at all 3 hole positions)
    # =================================================
    profile_cut_pts_template = [
        (71.75, -12.09),
        (65.00, -15.99),
        (58.25, -12.09),
        (58.25, -4.30),
        (65.00, -0.40),
        (71.75, -4.30),
    ]

    hole_x_positions = [65.00, -0.07, -64.98]
    
    profile_cut_plane = Plane.XZ.offset(-5)

    for hole_x in hole_x_positions:
        x_offset = hole_x - 65.00
        
        profile_cut_pts = [
            (pt[0] + x_offset, pt[1]) for pt in profile_cut_pts_template
        ]

        with BuildSketch(profile_cut_plane):
            Polygon(*profile_cut_pts)

        extrude(amount=32, mode=Mode.SUBTRACT)

    # =================================================
    # 8MM DIAMETER THROUGH HOLES - BOTTOM FACE
    # =================================================
    bottom_hole_positions = [
        (33.54, 20.78),
        (-33.69, 20.79),
    ]

    bottom_plane = Plane.XY.offset(-5)

    with BuildSketch(bottom_plane):
        for pt in bottom_hole_positions:
            with Locations(pt):
                Circle(4.0)

    extrude(amount=510, mode=Mode.SUBTRACT)

    # =================================================
    # NEW SVD PLANE FEATURES - 8MM DIAMETER HOLES
    # =================================================
    new_svd_hole_positions = [
        (140.00, 5.93),
        (15.97, 5.93),
    ]

    normal_vec = np.array([new_a, new_b, new_c])
    
    if abs(new_c) < 0.9:
        x_dir_temp = np.array([new_c, 0, -new_a])
    else:
        x_dir_temp = np.array([0, new_c, -new_b])
    
    x_dir_normalized = x_dir_temp / np.linalg.norm(x_dir_temp)
    y_dir_normalized = np.cross(normal_vec, x_dir_normalized)
    y_dir_normalized = y_dir_normalized / np.linalg.norm(y_dir_normalized)

    print(f"\nSVD Plane Vectors:")
    print(f"X-Dir = [{x_dir_normalized[0]:.6f}, {x_dir_normalized[1]:.6f}, {x_dir_normalized[2]:.6f}]")
    print(f"Y-Dir = [{y_dir_normalized[0]:.6f}, {y_dir_normalized[1]:.6f}, {y_dir_normalized[2]:.6f}]")

    try:
        svd_plane_custom = Plane(
            origin=new_pt1,
            x_dir=Vector(float(x_dir_normalized[0]), float(x_dir_normalized[1]), float(x_dir_normalized[2])),
            y_dir=Vector(float(y_dir_normalized[0]), float(y_dir_normalized[1]), float(y_dir_normalized[2]))
        )

        with BuildSketch(svd_plane_custom):
            for pt in new_svd_hole_positions:
                with Locations(pt):
                    Circle(4.0)

        extrude(amount=18, mode=Mode.SUBTRACT)
        print("\n✓ SVD Plane holes created successfully")
        
    except Exception as e:
        print(f"\n⚠ SVD Plane holes failed: {e}")
        try:
            fallback_plane = Plane.XZ.offset(-1.38)
            with BuildSketch(fallback_plane):
                for pt in new_svd_hole_positions:
                    with Locations(pt):
                        Circle(4.0)
            extrude(amount=10, mode=Mode.SUBTRACT)
            print("✓ Holes created using fallback XZ plane")
        except Exception as e2:
            print(f"✗ Fallback also failed: {e2}")

    # =================================================
    # HEXAGON SVD PLANE CUTS
    # =================================================
    hexagon_cut_positions = [
        (70.86, -9.03),
        (-60.15, -9.03),
    ]
    
    hex_radius = 7.0
    hex_angles = np.linspace(0, 2 * np.pi, 7)[:-1]
    hex_vertices = [(hex_radius * np.cos(angle), hex_radius * np.sin(angle)) 
                     for angle in hex_angles]
    
    print("\n" + "=" * 60)
    print("HEXAGON SVD PLANE CUTS")
    print("=" * 60)
    
    hex_normal_vec = hex_plane_normal
    
    if abs(hex_c) < 0.9:
        hex_x_dir_temp = np.array([hex_c, 0, -hex_a])
    else:
        hex_x_dir_temp = np.array([0, hex_c, -hex_b])
    
    hex_x_dir_normalized = hex_x_dir_temp / np.linalg.norm(hex_x_dir_temp)
    hex_y_dir_normalized = np.cross(hex_normal_vec, hex_x_dir_normalized)
    hex_y_dir_normalized = hex_y_dir_normalized / np.linalg.norm(hex_y_dir_normalized)
    
    try:
        hex_plane_custom = Plane(
            origin=centroid,
            x_dir=Vector(float(hex_x_dir_normalized[0]), float(hex_x_dir_normalized[1]), float(hex_x_dir_normalized[2])),
            y_dir=Vector(float(hex_y_dir_normalized[0]), float(hex_y_dir_normalized[1]), float(hex_y_dir_normalized[2]))
        )
        
        with BuildSketch(hex_plane_custom):
            for pos in hexagon_cut_positions:
                with Locations(pos):
                    Polygon(*hex_vertices)
        
        extrude(amount=550, mode=Mode.SUBTRACT)
        print("✓ Hexagon SVD plane cuts created successfully")
        
    except Exception as e:
        print(f"⚠ Hexagon cuts failed: {e}")
        try:
            fallback_hex_plane = Plane.XY.offset(-9.03)
            with BuildSketch(fallback_hex_plane):
                for pos in hexagon_cut_positions:
                    with Locations(pos):
                        Polygon(*hex_vertices)
            extrude(amount=-500, mode=Mode.SUBTRACT)
            print("✓ Hexagon cuts created using fallback XY plane")
        except Exception as e2:
            print(f"✗ Fallback also failed: {e2}")

    # =================================================
    # CHAMFER - 2.5x2.5mm
    # =================================================
    try:
        all_edges = new_part.edges()
        Chamfer(all_edges, 2.5)
        print("\n✓ Chamfer 2.5x2.5mm applied to all edges")
    except Exception as e:
        print(f"\n⚠ Chamfer failed: {e}")

# =====================================================
# EXPORT STL
# =====================================================
desktop_path = Path.home() / "Desktop"
stl_path = desktop_path / f"{part_name}.stl"

export_stl(new_part.part, str(stl_path))

print(f"\nSTL exported successfully:")
print(stl_path)

# =====================================================
# MASS PROPERTIES
# =====================================================
print(f"\nVolume (mm^3): {new_part.part.volume:.2f}")

cog = new_part.part.center(CenterOf.MASS)
print(f"Center of Gravity:")
print(f"X = {cog.X:.6f}")
print(f"Y = {cog.Y:.6f}")
print(f"Z = {cog.Z:.6f}")

# =====================================================
# OCP VIEW
# =====================================================
try:
    from ocp_vscode import show
    show(new_part.part)
    print("\nSent to OCP CAD Viewer.")
except Exception:
    print("\nOCP Viewer skipped - STL saved.")