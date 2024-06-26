import streamlit as st
import requests

st.title("Book Recommendation System")

st.write("""
### Ask for book recommendations
Type your query below to get book recommendations based on the top 100 books in any genre.
""")

if "recommendations" not in st.session_state:
    st.session_state.recommendations = []
if "selected_book" not in st.session_state:
    st.session_state.selected_book = None

query = st.text_input("Enter your query:")

if st.button("Get Recommendations"):
    if query:
        response = requests.get(f"http://127.0.0.1:8000/ask_book_recommendation?query={query}")
        if response.status_code == 200:
            st.session_state.recommendations = response.json().get("recommendations", [])
            st.session_state.selected_book = None
        else:
            st.write("Error fetching recommendations.")
    else:
        st.write("Please enter a query.")

if st.session_state.recommendations:
    st.write("### Book Recommendations:")
    book_titles = [book['book_title'] for book in st.session_state.recommendations]
    selected_book_title = st.selectbox("Select a book", book_titles, key="book_select")

    if st.button("Confirm Selection"):
        st.session_state.selected_book = next(
            (book for book in st.session_state.recommendations if book['book_title'] == selected_book_title), None)

if st.session_state.selected_book:
    selected_book = st.session_state.selected_book
    st.success(f"You selected: **{selected_book['book_title']}** by **{selected_book['author']}**")
    st.write("### Selected Book Details:")
    st.write(f"**Title**: {selected_book['book_title']}")
    st.write(f"**Author**: {selected_book['author']}")
    st.write(f"**Genre**: {selected_book['genre']}")
    st.write(f"**Rating**: {selected_book['rating']}")
    st.write(f"**Price**: ${selected_book['book_price']}")
    st.write(f"**Year**: {selected_book['year_of_publication']}")
    st.write("---")
