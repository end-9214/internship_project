import pandas as pd
from fastapi import FastAPI

# Load your dataset
df = pd.read_csv('/workspaces/codespaces-blank/amazon_bs_20102020.csv')

app = FastAPI()

@app.get("/top_100_books")
def get_top_100_books():
    return df.to_dict(orient="records")


@app.get("/book/{title}")
def get_book(title: str):
    book = df[df['Book_Title'].str.contains(title, case=False)].to_dict(orient="records")
    return book if book else {"message": "Book not found"}

@app.get("/close_task")
def close_task():
    return {"message": "Thank you for using the book recommendation agent!"}
