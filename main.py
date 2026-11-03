import os
import requests

API_KEY = os.environ.get("GEMINI_API_KEY")

def generate_telugu_fact():

    if not API_KEY:
        raise ValueError("GEMINI_API_KEY is missing")

    url = (
        "https://generativelanguage.googleapis.com/"
        "v1beta/models/gemini-3.8-flash:generateContent"
    )

    prompt = """
    Write one interesting and scientifically accurate
    fact for a Telugu YouTube Shorts video.

    Language: Telugu
    Duration: 30 seconds
    Include:
    1. Powerful opening hook
    2. Interesting explanation
    3. Exciting ending

    Return only the Telugu narration.
    """

    response = requests.post(
        url,
        params={"key": API_KEY},
        json={
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        },
        timeout=60
    )

    if response.status_code != 200:
        print("GEMINI ERROR:")
        print(response.text)
        raise Exception("Gemini API request failed")

    data = response.json()

    script = data["candidates"][0]["content"]["parts"][0]["text"]

    with open("script.txt", "w", encoding="utf-8") as f:
        f.write(script)

    print("SUCCESS! Telugu script generated.")
    print(script)


if __name__ == "__main__":
    generate_telugu_fact()
