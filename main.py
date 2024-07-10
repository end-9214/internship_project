from fastapi import FastAPI, HTTPException
import pandas as pd
from pydantic import BaseModel


df = pd.read_csv('/workspaces/internship_project/Top-100 Trending Books.csv')
df = df.dropna()

app = FastAPI()

class Book(BaseModel):
    book_title: str
    author: str
    genre: str
    rating: float
    book_price: float
    year_of_publication: int

@app.get("/top_100_books", response_model=list[Book])
def get_top_100_books(genre: str):
    filtered_df = df[df['genre'].str.contains(genre, case=False, na=False)]
    top_100_books = filtered_df.head(100).to_dict(orient='records')
    if not top_100_books:
        raise HTTPException(status_code=404, detail="No books found for the specified genre.")
    return top_100_books

@app.get("/top_10_books", response_model=list[Book])
def get_top_10_books(genre: str):
    filtered_df = df[df['genre'].str.contains(genre, case=False, na=False)]
    top_10_books = filtered_df.head(10).to_dict(orient='records')
    if not top_10_books:
        raise HTTPException(status_code=404, detail="No books found for the specified genre.")
    return top_10_books

@app.get("/select_book", response_model=Book)
def select_book(title: str):
    filtered_df = df[df['book_title'].str.contains(title, case=False, na=False)]
    if filtered_df.empty:
        raise HTTPException(status_code=404, detail="Book not found.")
    selected_book = filtered_df.iloc[0].to_dict()
    return selected_book

@app.get("/close_task")
def close_task():
    return {"message": "Thank you for using the book recommendation agent!"}
