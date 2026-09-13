import math

width = int(input("Enter horizontal resolution (pixels): "))
height = int(input("Enter vertical resolution (pixels): "))
diagonal = float(input("Enter physical diagonal size (inches): "))

total_pixels = width * height

gcd = math.gcd(width, height)
aspect_width = width // gcd
aspect_height = height // gcd

diagonal_pixels = math.sqrt(width**2 + height**2)
dpi = diagonal_pixels / diagonal

if dpi < 100:
    density = "Low Density (Standard Monitor)"
elif dpi <= 200:
    density = "Medium Density (HD Display)"
else:
    density = "High Density (Retina / Mobile)"

print("\n--- DISPLAY METRICS ANALYSIS ---")
print(f"Total Pixel Count : {total_pixels:,} pixels")
print(f"Aspect Ratio      : {aspect_width}:{aspect_height}")
print(f"Calculated DPI    : {dpi:.2f} DPI")
print(f"Density Category  : {density}")
