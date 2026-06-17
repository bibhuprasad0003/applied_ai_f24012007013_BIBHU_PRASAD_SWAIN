from transformers import pipeline

fill_mask = pipeline(
    task="fill-mask",
    model="bert-base-uncased"
)

text = "Artificial Intelligence is the [MASK] of future."

results = fill_mask(text)

for r in results:
    print(r["sequence"], " | score:", r["score"])