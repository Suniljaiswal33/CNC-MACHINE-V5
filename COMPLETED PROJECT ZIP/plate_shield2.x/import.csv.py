import csv
import os

# file path (change if needed)
dxf_path = os.path.expanduser("~/Desktop/plate_shield2.x.dxf")

points = []

# read dxf
with open(dxf_path, "r") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    if lines[i].strip() == "0" and i+1 < len(lines) and lines[i+1].strip() == "POINT":
        x = y = z = 0.0
        i += 2

        while i < len(lines) and lines[i].strip() != "0":
            code = lines[i].strip()
            value = lines[i+1].strip()

            if code == "10":
                x = float(value)
            elif code == "20":
                y = float(value)
            elif code == "30":
                z = float(value)

            i += 2

        points.append([x, y, z])
    else:
        i += 1

# output csv (same name)
csv_path = dxf_path.replace(".dxf", ".csv")

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["X", "Y", "Z"])
    writer.writerows(points)

print("✅ CSV saved at:", csv_path)