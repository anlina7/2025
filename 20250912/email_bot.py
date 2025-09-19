# TASKS:
# Classify incoming email (support, complain, etc.)
# Generate prompt for LLM
# Prepare LLM answer to that email

from google import genai
from config import API_KEY

client = genai.Client(api_key=API_KEY)

def classify_and_reply(email_body: str) -> str:
    prompt = (
        "Classify this email as one of: support, complaint, general, promo, spam. "
        "Then write a short reply suited to that category.\n"
        f"Email: {email_body}"
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

while True:
    email_body = input("Paste email body (or type 'quit' to exit): ")
    if email_body.lower() == "quit":
        break
    print("\n--- LLM Output ---")
    print(classify_and_reply(email_body))
    print("------------------\n")