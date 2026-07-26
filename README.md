# 📚 Platformă de Recenzii Cărți - Hackathon Project

Acesta este proiectul nostru pentru Hackathon. Este o aplicație web minimală care permite stocarea, vizualizarea și analizarea inteligentă a recenziilor de cărți. 

Aplicația este construită în Python (FastAPI) cu o bază de date SQLite (pentru portabilitate maximă) și integrează API-ul Google Gemini pentru a face analiza sentimentelor (Sentiment Analysis) pe recenziile adăugate de utilizatori.

## 🛠️ Tehnologii Folosite
* **Backend:** Python, FastAPI, SQLAlchemy
* **Frontend:** HTML5, Bootstrap, Vanilla JS (Jinja2 Templates)
* **Bază de date:** SQLite (local)
* **AI:** Google Gemini API (modelul `gemini-flash-latest`)

---

## 🚀 Cum să rulezi proiectul local

Urmați acești pași pentru a porni aplicația pe laptopurile voastre.

### Pasul 1: Clonarea și Mediul Virtual
1. Descărcați sau clonați acest folder pe laptopul vostru.
2. Deschideți un terminal în folderul proiectului.
3. Creați un mediu virtual pentru a nu amesteca pachetele de Python:
   * **Windows:** `python -m venv venv`
   * **Mac/Linux:** `python3 -m venv venv`
4. Activați mediul virtual:
   * **Windows:** `venv\Scripts\activate`
   * **Mac/Linux:** `source venv/bin/activate`

### Pasul 2: Instalarea pachetelor
Cu mediul virtual activat, rulați comanda:
`pip install -r requirements.txt`

### Pasul 3: Configurarea cheii API
Creați un fișier nou numit `.env` în folderul principal (lângă `main.py`) și adăugați cheia Gemini (cereți-i-o colegului care a generat-o):
`GEMINI_API_KEY=cheia_noastra_secreta_aici`

### Pasul 4: Popularea bazei de date (Pentru Testare Locală)
Pentru a avea date în aplicație înainte de workshop-ul de Azure, rulați scriptul de populare care va citi fișierul generat de AI din `/data/carti_generate.csv`:
`python populate_db.py`

### Pasul 5: Pornirea Serverului
Porniți aplicația rulând:
`python -m uvicorn main:app --reload`
*Aplicația va fi disponibilă în browser la adresa:* **http://127.0.0.1:8000**

---

## 📁 Structura Proiectului
* `main.py` - Logica principală (rutele FastAPI).
* `database.py` & `models.py` - Configurarea SQLite și structura tabelelor.
* `gemini_api.py` - Integrarea AI-ului pentru analiza sentimentului pe recenzii.
* `queries.py` - Cele 5 interogări SQL obligatorii (3x WHERE, 2x HAVING).
* `populate_db.py` - Script utilitar pentru a introduce CSV-ul în baza de date.
* `templates/` & `static/` - Interfața grafică.
* `data/` - Aici se află `carti_generate.csv` (setul nostru de date).

---

## 🎯 Ce mai avem de făcut (To-Do Luni)
Pentru a ne asigura că bifăm toate cerințele oficiale:
1. **Azure Data Factory (ADF):** Luni trebuie să folosim ADF pentru a importa oficial datele din fișierul nostru CSV într-o bază de date.
2. **PowerBI:** Trebuie să creăm două rapoarte vizuale pe baza setului nostru de date.
3. **Prezentarea (10 minute, toată echipa):** Trebuie să pregătim discursul de product management (nume produs, obiective, public țintă, nevoi rezolvate), să prezentăm rapoartele PowerBI și să facem demo-ul aplicației de față.
4. **Documentația:** Ne ocupăm luni, împreună.