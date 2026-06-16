from transformers import pipeline
bibhu = pipeline("ner",model="dbmdz/bert-large-cased-finetuned-conll03-english")
text = "Apple Inc. is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services. It is considered one of the Big Tech technology companies, alongside Amazon, Google, Microsoft, and Facebook."
result = bibhu(text)
print(result)
for entity in result:
    print(entity)