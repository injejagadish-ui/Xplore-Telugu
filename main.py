import os
import requests
import json

API_KEY = os.environ.get("GEMINI_API_KEY")

def generate_telugu_fact():

    if not API_KEY:
        raise ValueError("Gemini API key is missing")

    url = (
        "https://generativelanguage.googleapis.com/"
        "v1beta/models/gemini-2.5-flash:generateContent"
        f"?key={API_KEY}"
    )

    prompt = """
    Create one amazing and scientifically accurate fact
    for a Telugu YouTube Short.

    Requirements:
    - Telugu language
    - 30-second narration
    - Powerful opening hook
    - Interesting explanation
    - Exciting ending
    - Return only the narration.
    """

    response = requests.post(
        url,
        json={
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        },
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    script = data["candidates"][0]["content"]["parts"][0]["text"]

    print("TELUGU YOUTUBE SHORT SCRIPT")
    print("==========================")
    print(script)

    with open("script.txt", "w", encoding="utf-8") as file:
        file.write(script)


if __name__ == "__main__":
    generate_telugu_fact()
