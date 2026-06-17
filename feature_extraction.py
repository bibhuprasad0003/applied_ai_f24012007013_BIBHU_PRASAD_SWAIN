from transformers import pipeline

# Load feature extraction pipeline
extractor = pipeline("feature-extraction", model="distilbert-base-uncased")

# Input text
text = "Artificial Intelligence is amazing"

# Extract features
features = extractor(text)

# Print shape information
print("Number of tokens:", len(features[0]))
print("Embedding size per token:", len(features[0][0]))

# Print first token vector (sample)
print(features[0][0])