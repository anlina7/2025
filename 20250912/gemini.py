from google import genai
from config import API_KEY
# Initialize Gemini client
client = genai.Client(api_key= API_KEY)

while True:
    word = input("Enter a word (or 'quit' to exit): ").strip()
    if word.lower() == "quit":
        break

    prompt = f"Define the word '{word}' in simple terms."

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    print("Definition:", response.text.strip())
    from google import genai
from config import API_KEY

