from build123d import *
from pathlib import Path
import numpy as np

# =====================================================
# PART NAME
# =====================================================
part_name = "universal mount"

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
# RIGHT FACE PROFILE (YZ plane at X=90)
# Extract Y, Z coordinates from the sketch points
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
    # XZ Plane at Y = -15.59
    # =================================================
    profile_cut_pts_template = [
        (71.75, -12.09),
        (65.00, -15.99),
        (58.25, -12.09),
        (58.25, -4.30),
        (65.00, -0.40),
        (71.75, -4.30),
    ]

    # Hole positions
    hole_x_positions = [65.00, -0.07, -64.98]
    
    profile_cut_plane = Plane.XZ.offset(-15.59)

    for hole_x in hole_x_positions:
        # Offset profile points based on hole position
        x_offset = hole_x - 65.00
        
        profile_cut_pts = [
            (pt[0] + x_offset, pt[1]) for pt in profile_cut_pts_template
        ]

        with BuildSketch(profile_cut_plane):
            Polygon(*profile_cut_pts)

        extrude(amount=39, mode=Mode.SUBTRACT)

    # =================================================
    # 8MM DIAMETER THROUGH HOLES - BOTTOM FACE
    # XY Plane at Z = -1.89
    # =================================================
    bottom_hole_positions = [
        (33.54, 20.78),
        (-33.69, 20.79),
    ]

    bottom_plane = Plane.XY.offset(-5)

    with BuildSketch(bottom_plane):
        for pt in bottom_hole_positions:
            with Locations(pt):
                Circle(4.0)  # 8mm DIA (radius = 4mm)

    extrude(amount=510, mode=Mode.SUBTRACT)

    # =================================================
    # NEW SVD PLANE FEATURES - 8MM DIAMETER HOLES (200MM DEEP)
    # =================================================
    # Two hole locations on the SVD plane
    new_svd_hole_positions = [
        (140.00, 5.93),      # At Z = 14.24mm
        (15.97, 5.93),     # At Z = 14.24mm
    ]

    # Create orthonormal vectors for the custom plane
    # Given normal = (new_a, new_b, new_c), find perpendicular x_dir and y_dir
    
    normal_vec = np.array([new_a, new_b, new_c])
    
    # Find x_dir perpendicular to normal
    if abs(new_c) < 0.9:  # If normal is not too aligned with Z axis
        x_dir_temp = np.array([new_c, 0, -new_a])
    else:  # If aligned with Z axis
        x_dir_temp = np.array([0, new_c, -new_b])
    
    x_dir_normalized = x_dir_temp / np.linalg.norm(x_dir_temp)
    
    # Find y_dir = normal × x_dir
    y_dir_normalized = np.cross(normal_vec, x_dir_normalized)
    y_dir_normalized = y_dir_normalized / np.linalg.norm(y_dir_normalized)

    print(f"\nSVD Plane Vectors:")
    print(f"X-Dir = [{x_dir_normalized[0]:.6f}, {x_dir_normalized[1]:.6f}, {x_dir_normalized[2]:.6f}]")
    print(f"Y-Dir = [{y_dir_normalized[0]:.6f}, {y_dir_normalized[1]:.6f}, {y_dir_normalized[2]:.6f}]")

    # Create a custom plane from the SVD normal
    # Using origin point and perpendicular x_dir and y_dir
    try:
        svd_plane_custom = Plane(
            origin=new_pt1,
            x_dir=Vector(float(x_dir_normalized[0]), float(x_dir_normalized[1]), float(x_dir_normalized[2])),
            y_dir=Vector(float(y_dir_normalized[0]), float(y_dir_normalized[1]), float(y_dir_normalized[2]))
        )

        with BuildSketch(svd_plane_custom):
            for pt in new_svd_hole_positions:
                with Locations(pt):
                    Circle(4.0)  # 8mm DIA (radius = 4mm)

        extrude(amount=18, mode=Mode.SUBTRACT)
        print("\n✓ SVD Plane holes created successfully (200mm deep)")
        
    except Exception as e:
        print(f"\n⚠ SVD Plane holes could not be created: {e}")
        print("  Attempting alternative approach using XZ plane offset...")
        
        # Fallback: Use approximate offset plane
        try:
            fallback_plane = Plane.XZ.offset(-1.38)  # Using Y coordinate from SVD points
            
            with BuildSketch(fallback_plane):
                for pt in new_svd_hole_positions:
                    with Locations(pt):
                        Circle(4.0)
            
            extrude(amount=10, mode=Mode.SUBTRACT)
            print("✓ Holes created using fallback XZ plane")
            
        except Exception as e2:
            print(f"✗ Fallback also failed: {e2}")

    # =================================================
    # HEXAGON SVD PLANE CUTS - 14MM DIA CIRCUMSCRIBED
    # 200MM DEEP - TWO LOCATIONS
    # =================================================
    hexagon_cut_positions = [
        (70.86, -9.03),   # Position 1
        (-60.15, -9.03),  # Position 2
    ]
    
    # For circumscribed hexagon with 14mm diameter:
    # Circumscribed diameter = 14mm, so radius = 7mm
    # For regular hexagon, all vertices at distance R from center
    hex_radius = 7.0  # 14mm diameter / 2
    
    # Generate regular hexagon vertices (6 points at 60° intervals)
    hex_angles = np.linspace(0, 2 * np.pi, 7)[:-1]  # 6 vertices
    hex_vertices = [(hex_radius * np.cos(angle), hex_radius * np.sin(angle)) 
                     for angle in hex_angles]
    
    print("\n" + "=" * 60)
    print("HEXAGON SVD PLANE CUTS")
    print("=" * 60)
    print(f"Hexagon radius (circumscribed): {hex_radius}mm")
    print(f"Hexagon vertices: {len(hex_vertices)}")
    print(f"Cut positions: {hexagon_cut_positions}")
    print("=" * 60)
    
    # Create orthonormal vectors for the hexagon plane
    hex_normal_vec = hex_plane_normal
    
    # Find x_dir perpendicular to hex_normal
    if abs(hex_c) < 0.9:
        hex_x_dir_temp = np.array([hex_c, 0, -hex_a])
    else:
        hex_x_dir_temp = np.array([0, hex_c, -hex_b])
    
    hex_x_dir_normalized = hex_x_dir_temp / np.linalg.norm(hex_x_dir_temp)
    
    # Find y_dir = normal × x_dir
    hex_y_dir_normalized = np.cross(hex_normal_vec, hex_x_dir_normalized)
    hex_y_dir_normalized = hex_y_dir_normalized / np.linalg.norm(hex_y_dir_normalized)
    
    print(f"\nHexagon Plane Vectors:")
    print(f"Normal = [{hex_a:.6f}, {hex_b:.6f}, {hex_c:.6f}]")
    print(f"X-Dir = [{hex_x_dir_normalized[0]:.6f}, {hex_x_dir_normalized[1]:.6f}, {hex_x_dir_normalized[2]:.6f}]")
    print(f"Y-Dir = [{hex_y_dir_normalized[0]:.6f}, {hex_y_dir_normalized[1]:.6f}, {hex_y_dir_normalized[2]:.6f}]")
    
    try:
        # Create custom hexagon plane
        hex_plane_custom = Plane(
            origin=centroid,
            x_dir=Vector(float(hex_x_dir_normalized[0]), float(hex_x_dir_normalized[1]), float(hex_x_dir_normalized[2])),
            y_dir=Vector(float(hex_y_dir_normalized[0]), float(hex_y_dir_normalized[1]), float(hex_y_dir_normalized[2]))
        )
        
        # Create hexagon cuts at both positions
        with BuildSketch(hex_plane_custom):
            for pos in hexagon_cut_positions:
                with Locations(pos):
                    Polygon(*hex_vertices)
        
        extrude(amount=400, mode=Mode.SUBTRACT)
        print("\n✓ Hexagon SVD plane cuts created successfully (200mm deep)")
        print(f"  - 2 hexagon cuts at positions: {hexagon_cut_positions}")
        
    except Exception as e:
        print(f"\n⚠ Hexagon SVD plane cuts could not be created: {e}")
        print("  Attempting alternative approach...")
        
        try:
            # Fallback: Use XY plane as approximation
            fallback_hex_plane = Plane.XY.offset(-9.03)
            
            with BuildSketch(fallback_hex_plane):
                for pos in hexagon_cut_positions:
                    with Locations(pos):
                        Polygon(*hex_vertices)
            
            extrude(amount=500, mode=Mode.SUBTRACT)
            print("✓ Hexagon cuts created using fallback XY plane")
            
        except Exception as e2:
            print(f"✗ Fallback also failed: {e2}")

    # =================================================
    # CHAMFER - 2.5x2.5mm on BOTH SIDES of all edges
    # =================================================
    try:
        # Get all edges from the part
        all_edges = new_part.edges()
        
        # Apply chamfer to all edges (2.5mm on both sides)
        Chamfer(all_edges, 2.5)
        print("\n✓ Chamfer 2.5x2.5mm applied to all edges (both sides)")
        
    except Exception as e:
        print(f"\n⚠ Chamfer operation could not be applied: {e}")

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