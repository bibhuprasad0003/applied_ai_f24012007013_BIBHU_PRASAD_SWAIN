import torch
from transformers import AutoImageProcessor, AutoModel
from PIL import Image

# Load image
image = Image.open(r"C:\Users\user\Desktop\applied ai\image class.jpg.jpg").convert("RGB")

# Load processor and model
processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
model = AutoModel.from_pretrained("microsoft/resnet-50")

# Preprocess image
inputs = processor(images=image, return_tensors="pt")

# Extract features
with torch.no_grad():
    outputs = model(**inputs)

# Feature vector
features = outputs.last_hidden_state

print("Feature shape:", features.shape)