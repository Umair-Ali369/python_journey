import requests
from deep_translator import GoogleTranslator

def get_random_quote():
    try:
        quote = requests.get("https://type.fit/api/quotes", timeout=10)
        data = quote.json()
        return data
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.ConnectionError:
        return {"error": "No internet connection"}
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP error: {e}"}

def get_fact():
    try:
        quote = requests.get("https://catfact.ninja/fact", timeout=10)
        data = quote.json()
        return data
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.ConnectionError:
        return {"error": "No internet connection"}
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP error: {e}"}

def translate_text(text, target_lang, source_lan="auto"):
    try:
        translated = GoogleTranslator(source=source_lan, target=target_lang).translate(text)
        return translated
    except Exception as e:
        print(f"Error : {e}")

if __name__ == "__main__":
    text = "Welcome to NovxX, the future of communication."

    languages = {
        "ur": "Urdu",
        "ja": "Japanese",
        "ar": "Arabic",
        "fr": "French",
        "zh-CN": "Chinese"
    }

    for code, name in languages.items():
        result = translate_text(text, code)
        print(f"{name}: {result}")
