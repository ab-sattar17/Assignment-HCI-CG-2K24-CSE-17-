import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((300, 400, 3), dtype=np.uint8)

img[0:150, 0:200] = [255, 0, 0]
img[0:150, 200:400] = [0, 255, 0]
img[150:300, 0:200] = [0, 0, 255]
img[150:300, 200:400] = [255, 255, 255]

print("--- SYNTHETIC MATRIX METRICS ---")
print("Array Shape (H, W, C) :", img.shape)
print("Data Type             :", img.dtype)
print("Total Elements        :", img.size)
print("Memory Footprint      :", img.nbytes, "bytes")
print(f"Memory Footprint      : {img.nbytes / 1024:.2f} KB")

plt.figure(figsize=(8, 6))
plt.imshow(img)
plt.axis("off")
plt.title("300 × 400 Synthetic Image")
plt.show()
