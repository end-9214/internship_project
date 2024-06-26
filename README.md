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

  [![Watch the video](https://img.youtube.com/vi/VUoKC0wAGns/0.jpg)](https://youtu.be/VUoKC0wAGns)

## Why i use pipelines?
   
   In the `main.py` file, a pipeline from the Hugging Face `transformers` library is used even though the data is read from a CSV file.

   - The pipeline is utilized for understanding and processing user queries in natural language. This allows the system to interpret complex queries that might not be directly mapped to the data in the CSV file.
   - The `question-answering` pipeline helps in extracting relevant information from large text chunks. This is particularly useful when the query is more detailed or nuanced than just "top 100 books" or "top 10 books in a genre".

## How it works

   1. **Loading Data**:
   - The CSV file is read and preprocessed.

   2. **Generating Context Chunks**:
   - The dataset is divided into small chunks of text. This is done to ensure that the NLP model can process the text efficiently without running into memory issues.

   3. **Pipeline Utilization**:
   - The `transformers` pipeline is used to analyze these chunks of text. It uses a pretrained model (distilbert-base-uncased-distilled-squad) to understand the query and extract the most relevant information from the text.
   - This process helps in finding the best matches for the user’s query from the dataset.

   4. **Returning Recommendations**:
   - Based on the results from the pipeline, the system makes a list of recommendations that are then returned to the user.




   
