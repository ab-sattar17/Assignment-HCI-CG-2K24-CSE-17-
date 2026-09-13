from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open("sample.jpg").convert("RGB")
img = np.array(image)

red = img[:, :, 0]
green = img[:, :, 1]
blue = img[:, :, 2]

red_only = np.zeros_like(img)
green_only = np.zeros_like(img)
blue_only = np.zeros_like(img)

red_only[:, :, 0] = red
green_only[:, :, 1] = green
blue_only[:, :, 2] = blue

plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(red_only)
plt.title("Red Channel")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(green_only)
plt.title("Green Channel")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(blue_only)
plt.title("Blue Channel")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(red, cmap="gray")
plt.title("Red Intensity")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(green, cmap="gray")
plt.title("Green Intensity")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(blue, cmap="gray")
plt.title("Blue Intensity")
plt.axis("off")

plt.tight_layout()
plt.show()
