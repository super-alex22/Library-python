import streamlit as st

st.title("My Library App")

# 1. Safe Initialization
if "books" not in st.session_state:
    st.session_state["books"] = []

# ==========================================
# ➕ Add a book
# ==========================================
st.header("➕ Add a book")
title = st.text_input("Title")
author = st.text_input("Author")
price = st.number_input("Price", min_value=0.0)

if st.button("Add the book"):
    if title and author:
        book = {
            "title": title,
            "author": author,
            "price": price
        }
        st.session_state["books"].append(book)
        st.success(f"Success! '{title}' is now on the shelf.")
    else:
        st.warning("Please enter both title and author.")

# ==========================================
# 📚 Show all books
# ==========================================
if st.button("Show all books"):
    all_books = st.session_state["books"]
    if len(all_books) == 0:
        st.write("The library is empty. Go buy some books!")
    else:
        for book in all_books:
            st.write(f"**Title:** {book['title']}")
            st.write(f"**Author:** {book['author']}")
            st.write(f"**Price:** ${book['price']}")
            st.write("----------------------------")

# ==========================================
# 🔍 Search by author
# ==========================================
st.header("🔍 Search by author")
search_author = st.text_input("Enter author's name", key="author_search")
if st.button("Search by author"):
    found = False
    for book in st.session_state["books"]:
        if search_author.lower() in book["author"].lower():
            st.write(book)
            found = True
            
    if not found:
        st.write("No books from this author were found.")

# ==========================================
# 📖 Search by title
# ==========================================
st.header("📖 Search by title")
search_title = st.text_input("Enter book title", key="title_search")
if st.button("Search by title"):
    found = False
    for book in st.session_state["books"]:
        if search_title.lower() in book["title"].lower():
            st.write(book)
            found = True
            
    if not found:
        st.write("No books with this title were found.")

# ==========================================
# 💰 Statistics
# ==========================================
if st.button("Show the cheapest book"):
    books_list = st.session_state["books"]
    if len(books_list) == 0:
        st.write("Nothing to compare yet.")
    else:
        cheapest = min(books_list, key=lambda x: x["price"])
        st.write("The cheapest book is:", cheapest)
