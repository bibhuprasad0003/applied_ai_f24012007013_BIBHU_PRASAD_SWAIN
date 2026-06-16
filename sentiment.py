from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("I love this movie!")
print(result)   
result = classifier("I hate this movie!")
print(result)