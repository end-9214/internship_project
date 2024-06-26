import pandas as pd
from fastapi import FastAPI, Query, HTTPException
from transformers import pipeline
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load and preprocess the dataset
try:
    df = pd.read_csv('/workspaces/codespaces-blank/Top-100 Trending Books.csv')
    df = df.dropna()
    df['book_title'] = df['book_title'].str.strip()
    logger.info("Dataset loaded and preprocessed successfully.")
except Exception as e:
    logger.error(f"Error loading dataset: {e}")
    raise e

# Initialize the FastAPI app
app = FastAPI()

# Initialize the question-answering pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Function to generate context chunks from the dataset
def generate_context_chunks(df, chunk_size=1000):
    context_chunks = []
    current_chunk = ""
    for index, row in df.iterrows():
        book_info = f"Title: {row['book_title']}, Author: {row['author']}, Genre: {row['genre']}, Rating: {row['rating']}, Price: ${row['book_price']}, Year: {row['year_of_publication']}\n"
        if len(current_chunk) + len(book_info) > chunk_size:
            context_chunks.append(current_chunk)
            current_chunk = book_info
        else:
            current_chunk += book_info
    if current_chunk:
        context_chunks.append(current_chunk)
    return context_chunks

context_chunks = generate_context_chunks(df)

# Function to handle book recommendations
def get_book_recommendations(query, context_chunks):
    if re.match(r'top 100 books', query, re.IGNORECASE):
        return df.head(100).to_dict(orient="records")
    genre_match = re.match(r'top 10 books in (.+)', query, re.IGNORECASE)
    if genre_match:
        genre = genre_match.group(1)
        genre_books = df[df['genre'].str.contains(genre, case=False, na=False)]
        return genre_books.head(10).to_dict(orient="records")
    
    results = []
    for chunk in context_chunks:
        response = qa_pipeline(question=query, context=chunk)
        if response['answer'] not in results:
            results.append(response['answer'])
    return results

@app.get("/ask_book_recommendation")
def ask_book_recommendation(query: str = Query(..., description="Ask about top books")):
    try:
        recommendations = get_book_recommendations(query, context_chunks)
        if not recommendations:
            raise HTTPException(status_code=404, detail="No relevant books found.")
        return {"recommendations": recommendations}
    except Exception as e:
        logger.error(f"Error in book recommendation endpoint: {e}")
        raise HTTPException(status_code=500, detail="Error processing book recommendation query.")
