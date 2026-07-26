import os
import google.generativeai as genai
from dotenv import load_dotenv

# Incarcam variabilele de mediu din fisierul .env
load_dotenv()

# Configuram API-ul
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

def analyze_review_sentiment(review_text: str) -> str:
    """
    Foloseste modelul Gemini pentru a analiza sentimentul unei recenzii.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Analizeaza urmatoarea recenzie de carte si spune-mi daca sentimentul este Strict Pozitiv, Negativ sau Neutru. Ofera doar un cuvant ca raspuns. Recenzia: '{review_text}'"
        
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Eroare la apelarea Gemini API: {str(e)}"