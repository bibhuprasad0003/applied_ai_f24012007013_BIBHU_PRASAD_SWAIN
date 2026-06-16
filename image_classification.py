from transformers import pipeline
from PIL import Image
classifier = pipeline("image-classification")
image = Image.open("C:\\Users\\user\\Desktop\\applied ai\\image class.jpg.jpg")
result = classifier(image)
print(result)