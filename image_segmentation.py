import torch
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForSemanticSegmentation

# Load image
image = Image.open(r"C:\Users\user\Desktop\applied ai\image class.jpg.jpg").convert("RGB")

# Load processor & model
processor = AutoImageProcessor.from_pretrained(
    "nvidia/segformer-b0-finetuned-ade-512-512"
)
model = AutoModelForSemanticSegmentation.from_pretrained(
    "nvidia/segformer-b0-finetuned-ade-512-512"
)

# Preprocess image
inputs = processor(images=image, return_tensors="pt")

# Forward pass
with torch.no_grad():
    outputs = model(**inputs)

# Get segmentation map
logits = outputs.logits
segmentation = logits.argmax(dim=1)[0]

# Convert to numpy
segmentation = segmentation.cpu().numpy()

# Display
plt.imshow(segmentation)
plt.title("Segmentation Map")
plt.axis("off")
plt.show()