from transformers import pipeline

def transformer_task(task_name, input_data):

    if task_name == "sentiment-analysis":
        pipe = pipeline("sentiment-analysis")
        return pipe(input_data)

    if task_name == "text-generation":
        pipe = pipeline("text-generation", model="gpt2")
        return pipe(input_data, max_new_tokens=50)

    if task_name == "summarization":
        pipe = pipeline("summarization")
        return pipe(input_data)

    if task_name == "translation":
        pipe = pipeline("translation_en_to_fr")
        return pipe(input_data)

    if task_name == "question-answering":
        pipe = pipeline("question-answering")
        return pipe(
            question=input_data["question"],
            context=input_data["context"]
        )

    return "Unsupported task"
result = transformer_task(
    "text-generation",
    "Artificial Intelligence will"
)

print(result)
