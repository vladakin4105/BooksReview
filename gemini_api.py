import os
import requests
from dotenv import load_dotenv

# Incarcam variabilele de mediu din fisierul .env
load_dotenv()

# Preluam cheia din .env
API_KEY = os.getenv("GEMINI_API_KEY")

def get_book_recommendation(favorite_books: list) -> str:
    """
    Cere API-ului Gemini o recomandare bazată pe cărțile favorite din baza de date.
    Returnează doar titlul și autorul.
    """
    if not favorite_books:
        return "Nu ai nicio carte adăugată la favorite. Adaugă câteva pentru a primi o recomandare personalizată!"
        
    lista_carti = ", ".join(favorite_books)
    
    # Am modificat prompt-ul pentru a fi foarte restrictiv cu Gemini
    prompt = f"Următoarele cărți sunt favoritele mele: {lista_carti}. Pe baza acestora, recomandă-mi o singură carte nouă de citit (care să nu fie în această listă). Trebuie să răspunzi STRICT cu titlul cărții și autorul, în formatul 'Titlu de Autor', fără absolut nicio altă explicație, salut, sau text suplimentar."
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()
        
        if response.status_code == 200:
            return response_data['candidates'][0]['content']['parts'][0]['text'].strip()
        else:
            return "Eroare la generarea recomandării."
            
    except Exception as e:
        return f"Eroare la conexiunea HTTP: {str(e)}"