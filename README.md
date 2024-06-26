# Book Recommendation System

This project is a Book Recommendation System built using FastAPI for the backend and Streamlit for the frontend. The system processes user queries to recommend books based on a dataset of the top 100 trending books.

## Features

- Allows users to query for book recommendations based on genres.
- Users can select a book from the recommendations and view detailed information about the selected book.

## Technologies Used

- **FastAPI**: For building the backend API.
- **Streamlit**: For creating the frontend user interface.
- **Transformers**: Using Hugging Face's `pipeline` for question-answering.
- **Pandas**: For data manipulation and preprocessing.
- **Python**: The programming language used to develop this system.

## Dataset

The dataset used in this project is the "Top 100 Trending Books" dataset. 
Dataset link - https://www.kaggle.com/datasets/anshtanwar/top-200-trending-books-with-reviews

## How to Use

### Prerequisites

- Required Python packages: `fastapi`, `pandas`, `transformers`, `streamlit`, `requests`, `uvicorn`

### Setup

1. **Clone the Repository**

   ```sh
   git clone https://github.com/end-9214/internship_project.git
   cd <repository-directory>

2. **Install requirements**

   ```sh
   pip install -r requirements.txt

3. **Start the app**

   ```sh
    uvicorn main:app --reload
    ```

   ```sh
    streamlit run app.py
    ```

### DEMO VIDEO

  

   
