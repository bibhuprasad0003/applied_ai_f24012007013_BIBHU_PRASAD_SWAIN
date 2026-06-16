from transformers import pipeline
qa=pipeline("document-question-answering",model="google/flan-t5-base")
result=qa(question="What is the capital of France?")
print(result)