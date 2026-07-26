import os
import requests
from dotenv import load_dotenv

# Incarcam variabilele de mediu din fisierul .env
load_dotenv()

# Preluam cheia din .env
API_KEY = os.getenv("GEMINI_API_KEY")

def analyze_review_sentiment(review_text: str) -> str:
    """
    Foloseste direct REST API-ul Gemini.
    Folosim pointer-ul 'gemini-flash-latest' pentru a evita deprecierile.
    """
    prompt = f"Analizeaza urmatoarea recenzie de carte si spune-mi daca sentimentul este Strict Pozitiv, Negativ sau Neutru. Ofera doar un cuvant ca raspuns. Recenzia: '{review_text}'"
    
    # URL-ul actualizat cu alias-ul universal pentru ultima versiune disponibila gratuit
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()
        
        if response.status_code == 200:
            sentiment = response_data['candidates'][0]['content']['parts'][0]['text']
            return sentiment.strip()
        else:
            error_msg = response_data.get('error', {}).get('message', 'Eroare necunoscuta')
            return f"Eroare REST API ({response.status_code}): {error_msg}"
            
    except Exception as e:
        return f"Eroare la conexiunea HTTP: {str(e)}"