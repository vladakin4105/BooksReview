import os
import requests
from dotenv import load_dotenv

# Incarcam cheia din .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Eroare: Nu am găsit cheia API în fișierul .env")
    exit()

print("Interogăm serverele Google... ⏳\n")

# Facem un call către endpoint-ul care listează toate modelele
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
response = requests.get(url)

if response.status_code == 200:
    models = response.json().get('models', [])
    print("✅ Modele disponibile pentru generare text pe contul tău:")
    print("-" * 50)
    for m in models:
        # Afișăm doar modelele care suportă generare de text
        if 'generateContent' in m.get('supportedGenerationMethods', []):
            print(m['name'])
    print("-" * 50)
else:
    print(f"❌ Eroare la interogare ({response.status_code}): {response.text}")