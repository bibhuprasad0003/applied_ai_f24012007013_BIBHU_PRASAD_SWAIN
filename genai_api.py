from google import genai

client= genai.Client(api_key="AQ.Ab8RN6LEdqLUhHyZcQYeZpjjDJXqLk2Ai1yNxGFgM9j5VCbnCQ")

while True:
    question = input("you: ")
    
    if question.lower() == "exit":
        print("Goodbye!")
        break
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )
    print(f"gemini: {response.text}")