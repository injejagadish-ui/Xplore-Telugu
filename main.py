import os
import time
import requests

API_KEY = os.environ.get("GEMINI_API_KEY")

def generate_telugu_fact():

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing")

models = [
    "gemini-3.8-flash",
    "gemini-3.5-flash-lite"
]

prompt = """
Write one interesting and scientifically accurate
fact for a Telugu YouTube Shorts video.

Language: Telugu
Duration: 30 seconds.

Include:
1. Powerful opening hook
2. Interesting explanation
3. Exciting ending

Return only the Telugu narration.
"""

for model in models:
    print("Trying model:", model)

    url = (
        "https://generativelanguage.googleapis.com/"
        f"v1beta/models/{model}:generateContent"
    )

    for attempt in range(3):
        try:
            response = requests.post(
                url,
                params={"key": API_KEY},
                json={
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }]
                },
                timeout=90
            )

            if response.status_code == 503:
                wait = 10 * (2 ** attempt)
                print(f"Server busy. Retrying in {wait} seconds...")
                time.sleep(wait)
                continue

            if response.status_code == 429:
                wait = 20 * (2 ** attempt)
                print(f"Rate limited. Retrying in {wait} seconds...")
                time.sleep(wait)
                continue

            response.raise_for_status()

            data = response.json()
            script = data["candidates"][0]["content"]["parts"][0]["text"]

            with open("script.txt", "w", encoding="utf-8") as f:
                f.write(script)

            print("SUCCESS! Telugu script generated.")
            print(script)
            return

        except requests.exceptions.RequestException as error:
            print("Request error:", error)
            if attempt == 2:
                break
            time.sleep(10 * (2 ** attempt))

raise Exception("All Gemini models failed. Please try again later.")

if name == "main":
generate_telugu_fact()
