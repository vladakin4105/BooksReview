from sqlalchemy.orm import Session
from sqlalchemy import func
from models import Book, Review


def get_books_by_genre(db: Session, target_genre: str):
    """1. WHERE: Aducem toate cartile dintr-un anumit gen."""
    return db.query(Book).filter(Book.genre == target_genre).all()

def get_reviews_above_rating(db: Session, min_rating: float):
    """2. WHERE: Aducem toate recenziile cu nota mai mare decat min_rating."""
    return db.query(Review).filter(Review.rating >= min_rating).all()

def get_books_by_author(db: Session, author_name: str):
    """3. WHERE: Cautam cartile unui anumit autor."""
    return db.query(Book).filter(Book.author == author_name).all()



def get_genres_with_multiple_books(db: Session, min_books: int = 2):
    """4. HAVING: Gasim genurile literare care au mai mult de X carti in baza de date."""
    return db.query(
        Book.genre, func.count(Book.id).label('book_count')
    ).group_by(Book.genre).having(func.count(Book.id) >= min_books).all()

def get_books_with_high_average_rating(db: Session, min_avg_rating: float = 4.0):
    """5. HAVING: Gasim cartile care au o nota medie mai mare sau egala cu min_avg_rating."""
    return db.query(
        Review.book_id, func.avg(Review.rating).label('average_rating')
    ).group_by(Review.book_id).having(func.avg(Review.rating) >= min_avg_rating).all()