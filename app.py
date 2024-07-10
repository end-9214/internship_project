import streamlit as st
import requests

st.title("Book Recommendation System")

# Initialize session state
if "recommendations" not in st.session_state:
    st.session_state.recommendations = []
if "selected_book" not in st.session_state:
    st.session_state.selected_book = None

# Selection for Genre Browsing
st.write("""
### Browse books by genre
""")

genre = st.text_input("Enter genre for top books:")

if st.button("Get Top 100 Books"):
    if genre:
        response = requests.get(f"http://127.0.0.1:8000/top_100_books?genre={genre}")
        if response.status_code == 200:
            st.session_state.recommendations = response.json()
            st.session_state.selected_book = None
        else:
            st.error("Error fetching top 100 books.")
    else:
        st.error("Please enter a genre.")

if st.button("Get Top 10 Books"):
    if genre:
        response = requests.get(f"http://127.0.0.1:8000/top_10_books?genre={genre}")
        if response.status_code == 200:
            st.session_state.recommendations = response.json()
            st.session_state.selected_book = None
        else:
            st.error("Error fetching top 10 books.")
    else:
        st.error("Please enter a genre.")

if st.session_state.recommendations:
    st.write("### Book Recommendations:")
    book_titles = [book['book_title'] for book in st.session_state.recommendations]
    selected_book_title = st.selectbox("Select a book", book_titles, key="book_select_genre")

    if st.button("Confirm Selection", key="confirm_genre"):
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

    st.write("Thank you for using the Book Recommendation System!")
    if st.button("Close"):
        st.session_state.recommendations = []
        st.session_state.selected_book = None
        st.experimental_rerun()
