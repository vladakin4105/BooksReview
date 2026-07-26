import csv
from database import SessionLocal
import models

def populate_books_from_csv(file_path):
    # Deschidem sesiunea de baza de date
    db = SessionLocal()
    
    try:
        # Deschidem fisierul CSV
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            books_added = 0
            for row in csv_reader:
                # Cream un obiect Book pentru fiecare rand din CSV
                new_book = models.Book(
                    title=row['title'].strip(),
                    author=row['author'].strip(),
                    genre=row['genre'].strip(),
                    description=row['description'].strip()
                )
                db.add(new_book)
                books_added += 1
            
            # Salvam modificarile in baza de date
            db.commit()
            print(f"Succes! Au fost adaugate {books_added} carti in baza de date.")
    
    except FileNotFoundError:
        print(f"Eroare: Nu am gasit fisierul {file_path}. Asigura-te ca e in folderul /data.")
    except Exception as e:
        print(f"A aparut o eroare: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    # Rulam functia
    print("Incepem popularea bazei de date...")
    populate_books_from_csv("data/books_generate.csv")