from transformers import pipeline
from PIL import Image
import matplotlib.pyplot as plt

# Load depth estimation pipeline
depth_estimator = pipeline("depth-estimation")

# Load image
image = Image.open(r"C:\Users\user\Desktop\applied ai\image class.jpg.jpg")  # replace with your image path

# Perform depth estimation
result = depth_estimator(image)

# Extract depth map
depth_map = result["depth"]

# Show original image
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)
plt.axis("off")

# Show depth map
plt.subplot(1, 2, 2)
plt.title("Depth Map")
plt.imshow(depth_map, cmap="gray")
plt.axis("off")

plt.show()