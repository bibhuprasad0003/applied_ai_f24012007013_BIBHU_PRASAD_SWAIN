from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
prompt = "the future of AI in education is"
output = generator(prompt, max_length=50)
print(output)