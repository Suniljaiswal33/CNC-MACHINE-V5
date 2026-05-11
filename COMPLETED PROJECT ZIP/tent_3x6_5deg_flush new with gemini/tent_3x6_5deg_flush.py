import os
import ezdxf
from build123d import *

# =========================
# PATHS
# =========================
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
DXF_PATH = os.path.join(desktop, "tent_3x6_5deg_flush.dxf")
STL_FILE = os.path.join(desktop, "tent_3x6_5deg_flush.stl")

HEIGHT = 40
EXTRA_HEIGHT = 125
TARGET_VOLUME = 2.560e7

# =========================
# GEOMETRY DATA
# =========================
red_loops = [
    [  # TOP LEFT RED
        (-1036.8038, 575.1623), (-1129.6117, 637.0766), (-1166.8687, 648.8822),
        (-1171.4368, 649.2799), (-1179.5592, 648.3249), (-1186.7362, 645.2796),
        (-1193.1979, 640.3746), (-1285.8432, 520.9098), (-1293.0621, 508.1550),
        (-1295.4957, 501.4600), (-1297.0811, 494.6998), (-1297.9280, 481.9838),
        (-1296.4187, 469.8180), (-1293.4535, 458.6993), (-1287.2314, 444.2989),
        (-1280.4694, 433.3214), (-1271.0020, 421.1579), (-1221.6131, 374.8174),
        (-1192.1817, 406.9061), (-1193.1508, 414.5228), (-1191.3429, 421.7225),
        (-1188.8153, 425.3731), (-1181.1758, 430.1556), (-1171.7440, 432.9725),
        (-1158.2425, 435.0003), (-1141.2100, 439.7477), (-1130.7637, 445.1681),
        (-1117.2410, 456.2751), (-1109.7881, 465.1590), (-1101.3262, 480.2576),
        (-1097.9800, 491.2779), (-1095.8075, 507.6965), (-1093.6829, 517.5363),
        (-1088.4705, 525.9797), (-1082.3968, 530.1940), (-1075.3334, 532.5385),
    ],
    [  # BOTTOM LEFT RED
        (-859.9372, -495.8032), (-1064.3368, -495.8032), (-1079.1092, -495.3481),
        (-1094.9116, -493.3615), (-1113.3513, -488.2623), (-1126.1872, -481.0549),
        (-1132.8419, -475.3328), (-1141.5957, -462.0892), (-1145.1755, -452.0084),
        (-1146.2952, -445.7001), (-1167.6708, -266.8892), (-1109.2595, -281.4287),
        (-1105.9182, -286.6616), (-1100.5247, -294.2078), (-1096.1553, -298.4976),
        (-1091.2492, -302.0278), (-1085.8085, -304.6402), (-1081.3111, -305.9819),
        (-1067.1993, -303.5044), (-1055.2861, -301.6028), (-1040.1036, -301.3219),
        (-1026.8411, -302.2782), (-1014.2711, -305.0622), (-1002.3846, -309.9061),
        (-991.5376, -316.6650), (-982.0550, -325.1362), (-974.2211, -335.0660),
        (-968.2705, -346.1569), (-964.9714, -355.5155), (-962.9709, -364.2003),
        (-962.3702, -376.7358), (-962.0577, -387.4881), (-960.3855, -396.7796),
        (-957.2590, -406.7350), (-952.5033, -416.1985), (-946.8150, -424.6964),
        (-937.5605, -434.5028), (-928.5622, -441.0478), (-918.0825, -446.3701),
        (-902.6564, -450.0568),
    ]
]

top_right_loop = [
    (-135.4127, 380.4626), (91.5498, 380.4626), (107.4089, 376.8319),
    (114.2609, 371.9141), (121.2297, 363.2956), (127.0492, 353.0723),
    (130.6822, 344.4130), (133.6745, 333.7199), (135.0214, 325.2342),
    (135.2770, 320.5468), (135.5325, 102.1456), (89.6949, 102.1456),
    (84.8033, 116.2491), (78.4856, 129.3130), (67.0178, 143.0557),
    (51.9900, 152.3563), (37.0533, 155.2293), (14.0619, 153.6852),
    (-13.0353, 157.8885), (-24.3472, 162.8135), (-39.1866, 173.5524),
    (-47.4700, 182.3974), (-57.0310, 197.7134), (-60.9485, 209.0503),
    (-62.8779, 220.8524), (-62.7669, 232.7991), (-59.6359, 249.1829),
    (-58.1900, 267.8799), (-60.5588, 281.6756), (-66.4165, 294.4988),
    (-77.9268, 309.3920), (-88.4413, 318.5932), (-101.8123, 327.3827),
    (-118.2274, 333.2964), (-135.4127, 335.5166),
]

top_right_bottom_loop = [
    (93.0481, -132.3319), (135.5325, -132.3319), (135.1344, -303.1169),
    (131.8929, -322.8752), (128.9924, -332.1887), (126.8897, -338.2992),
    (121.1591, -349.7708), (117.6160, -355.1438), (111.2815, -362.3674),
    (103.9545, -368.3353), (92.2280, -373.4654), (85.1643, -374.8321),
    (77.0562, -375.3079), (-90.2294, -375.3079), (-91.7343, -329.9876),
    (-86.1211, -329.9876), (-79.3741, -329.3358), (-75.3010, -328.0629),
    (-70.2396, -325.3750), (-67.3810, -322.8435), (-63.1258, -316.3233),
    (-60.7929, -311.1479), (-59.4038, -306.4913), (-57.9399, -299.5335),
    (-56.6288, -289.5456), (-55.9671, -278.2083), (-55.7004, -268.7734),
    (-54.9751, -257.4691), (-52.6407, -244.8871), (-50.8927, -238.6959),
    (-45.1829, -227.1005), (-37.4382, -216.6552), (-22.3858, -204.0825),
    (-10.7811, -197.8648), (5.0580, -192.9340), (21.5601, -191.3406),
    (40.1092, -192.7773), (48.8783, -193.6667), (58.9795, -191.5486),
    (68.5650, -186.5445), (74.7705, -181.3166), (81.6487, -172.6455),
    (87.0815, -162.3802), (90.1400, -153.4232), (91.7854, -146.0167),
    (92.7697, -137.1418),
]

# =========================
# BUILD PART
# =========================
with BuildPart() as main:
    # 1. LOAD DXF
    if not os.path.exists(DXF_PATH):
        raise FileNotFoundError(f"❌ DXF not found at {DXF_PATH}")
    
    doc = ezdxf.readfile(DXF_PATH)
    msp = doc.modelspace()
    loops = []
    for e in msp:
        if e.dxftype() == "LWPOLYLINE" and e.closed:
            loops.append([(p[0], p[1]) for p in e.get_points()])
    
    if not loops:
        raise ValueError("❌ No closed polylines in DXF")

    def get_area(p):
        return abs(sum(p[i][0]*p[(i+1)%len(p)][1] - p[(i+1)%len(p)][0]*p[i][1] for i in range(len(p)))/2)
    
    loops.sort(key=get_area, reverse=True)
    outer_poly = loops[0]
    inner_polys = loops[1:]

    # Base Extrusion
    with BuildSketch() as base_sketch:
        with BuildLine():
            Polyline(*outer_poly, close=True)
        make_face()
    extrude(amount=HEIGHT)

    # Cut Holes from DXF
    for loop in inner_polys:
        with BuildSketch(Plane.XY):
            with BuildLine():
                Polyline(*loop, close=True)
            make_face()
        extrude(amount=HEIGHT, mode=Mode.SUBTRACT)

    # 2. Add Red Profiles
    for loop in red_loops:
        with BuildSketch(Plane.XY.offset(HEIGHT)):
            with BuildLine():
                Polyline(*loop, close=True)
            make_face()
        extrude(amount=EXTRA_HEIGHT, mode=Mode.ADD)

    # 3. Top Right Slopes
    for loop in [top_right_loop, top_right_bottom_loop]:
        with BuildSketch(Plane.XY.offset(HEIGHT)):
            with BuildLine():
                Polyline(*loop, close=True)
            make_face()
        extrude(amount=30, taper=-5, mode=Mode.ADD)

    # 4. Tapered Holes (Cones)
    taper_pts = [(-1100.9398, 76.1796), (-254.1743, -373.8205), (75.4415, 316.1796)]
    for pt in taper_pts:
        with Locations((pt[0], pt[1], HEIGHT + 65)): 
            Cone(bottom_radius=20, top_radius=40, height=165, mode=Mode.SUBTRACT)

    # 5. Ø105 Cuts
    points_105 = [
        (-1196.2731, 522.0859, 165), (-1076.3649, -403.8204, 165),
        (33.6351, -283.8205, 70), (13.6351, 226.1796, 70),
    ]
    for x, y, z in points_105:
        with Locations((x, y, z - 5)): 
            Cylinder(radius=105/2, height=10, mode=Mode.SUBTRACT)

# =========================
# VOLUME & SCALING
# =========================
res = main.part

# Apply Fillet to top face edges
try:
    top_face = res.faces().sort_by(Axis.Z)[-1]
    res = fillet(top_face.edges(), radius=5)
except:
    print("⚠️ Warning: Fillet failed on some edges, skipping to preserve geometry.")

# Calculate Scaling for Target Volume
vol_initial = res.volume
scale_fact = (TARGET_VOLUME / vol_initial) ** (1/3)
res = res.scale(scale_fact)

print(f"\n--- VOLUME REPORT ---")
print(f"Target Volume:         {TARGET_VOLUME}")
print(f"Volume Before Scaling: {vol_initial:.2f}")
print(f"Applied Scale Factor:  {scale_fact:.6f}")
print(f"Volume After Scaling:  {res.volume:.2f}")

# Final Unit Fix (Scale by 0.1)
res = res.scale(0.1)
print(f"Final Export Volume:   {res.volume:.2f}")

# =========================
# EXPORT & PREVIEW
# =========================
export_stl(res, STL_FILE)
print(f"\n✅ SUCCESS: STL saved to {STL_FILE}")

# Fixed Preview logic
try:
    from ocp_vscode import show, set_port
    # Explicitly set the port to match your VSCode settings (default is 3939)
    set_port(3939) 
    show(res)
except Exception as e:
    print(f"📡 Preview skipped or OCP-VSCode not responding: {e}")