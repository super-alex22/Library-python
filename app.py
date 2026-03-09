import streamlit as st

st.title("My Library App")

# Check if the list exists, if not - create it
if "books" not in st.session_state:
    st.session_state.books = []

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
        st.session_state.books.append(book)
        st.success("The book has been added successfully!")
    else:
        st.warning("Please enter both title and author. Even a ghostwriter has a name!")

# ==========================================
# 📚 Show all books
# ==========================================
if st.button(" Show all books"):
    if len(st.session_state.books) == 0:
        st.write("No books added yet. The shelves are gathering dust.")
    else:
        for book in st.session_state.books:
            st.write("Title:", book["title"])
            st.write("Author:", book["author"])
            st.write("Price:", book["price"])
            st.write("----------------------------")

# ==========================================
# 🔍 Search by author
# ==========================================
st.header("🔍 Search by author")
search_author = st.text_input("Enter author's name")
if st.button("Search by author"):
    found = False
    
    for book in st.session_state.books:
        if book["author"].lower() == search_author.lower():
            st.write(book)
            found = True
            
    if found == False:
        st.write("No books from this author were found.")

# ==========================================
# 📖 Search by title
# ==========================================
st.header("📖 Search by title")
search_title = st.text_input("Enter book title")
if st.button("Search by title"):
    found = False
    
    for book in st.session_state.books:
        if book["title"].lower() == search_title.lower():
            st.write(book)
            found = True
            
    if found == False:
        st.write("No books with this title were found.")

# ==========================================
# 💰 Statistics
# ==========================================
if st.button("Show the cheapest book"):
    if len(st.session_state.books) == 0:
        st.write("Nothing to compare. Prices are currently imaginary.")
    else:
        cheapest = st.session_state.books[0]
        for book in st.session_state.books:
            if book["price"] < cheapest["price"]:
                cheapest = book
        st.write("The cheapest book is:", cheapest)
