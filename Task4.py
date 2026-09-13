from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open("sample.jpg").convert("RGB")
img = np.array(image)

N = 8

original_height, original_width, channels = img.shape

downsampled = img[::N, ::N, :]

expanded = np.repeat(downsampled, N, axis=0)
expanded = np.repeat(expanded, N, axis=1)

expanded = expanded[:original_height, :original_width, :]

original_memory = img.nbytes
downsampled_memory = downsampled.nbytes

height_reduction = (1 - downsampled.shape[0] / original_height) * 100
width_reduction = (1 - downsampled.shape[1] / original_width) * 100
memory_reduction = (1 - downsampled_memory / original_memory) * 100

print("--- SPATIAL DOWNSAMPLING ANALYSIS ---")
print("Original Shape       :", img.shape)
print("Downsampled Shape    :", downsampled.shape)
print("Re-expanded Shape    :", expanded.shape)
print("Downsampling Factor  :", N)
print(f"Height Reduction     : {height_reduction:.2f}%")
print(f"Width Reduction      : {width_reduction:.2f}%")
print(f"Memory Reduction     : {memory_reduction:.2f}%")

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(downsampled)
plt.title("Downsampled Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(expanded)
plt.title("Re-expanded / Pixelated Image")
plt.axis("off")

plt.tight_layout()
plt.show()
