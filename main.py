from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import database
import models
import gemini_api

# Cream tabelele in baza de date SQLite daca nu exista
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Book Reviews Hackathon API")

# Setam folderele pentru HTML, CSS, JS
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Ruta principala (Frontend - Interfata minimala)
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session = Depends(database.get_db)):
    # Aducem toate cartile pentru a le afisa pe prima pagina
    books = db.query(models.Book).all()
    return templates.TemplateResponse(request=request, name="index.html", context={"books": books})

# Ruta API pentru a adauga o carte (Utila pt teste manuale pana faceti pipeline-ul in ADF)
@app.post("/api/books")
async def create_book(title: str = Form(...), author: str = Form(...), genre: str = Form(...), description: str = Form(...), db: Session = Depends(database.get_db)):
    new_book = models.Book(title=title, author=author, genre=genre, description=description)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# Ruta API care apeleaza Gemini pentru analiza recenziei
@app.post("/api/analyze-review")
async def analyze_review(review_text: str = Form(...)):
    # Apelam functia scrisa de noi din gemini_api.py
    sentiment = gemini_api.analyze_review_sentiment(review_text)
    return {"original_text": review_text, "sentiment_gemini": sentiment}