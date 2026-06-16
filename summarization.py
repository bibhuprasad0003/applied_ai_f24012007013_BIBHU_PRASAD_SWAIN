from transformers import pipeline
bibhu = pipeline("summarization",model="facebook/bart-large-cnn")
text = """The field of artificial intelligence (AI) has seen significant advancements in recent years, with applications ranging from natural language processing to computer vision. AI has the potential to revolutionize various industries, including healthcare,

finance, and transportation. However, there are also concerns about the ethical implications of AI, such as job displacement and privacy issues. As AI continues to evolve, it is crucial to address these challenges and ensure that the technology is developed and used responsibly."""
summary = bibhu(text, max_length=100, min_length=30, do_sample=False
)
print(summary[0]['summary_text'])