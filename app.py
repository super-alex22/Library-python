import streamlit as st

st.title("My Library App")
@st.dialog("⚠️ SYSTEM CRITICAL ERROR")
def show_scary_popup(book_to_kill, math_result):
    st.error("DATABASE BREACH DETECTED!")
    st.write(f"Are you sure you want to delete '{book_to_kill['title']}'?")
    
    if st.button("CONFIRM DESTRUCTION"):
        if math_result == 20:
            st.session_state["books"].remove(book_to_kill)
            st.success("Data wiped.")
            st.rerun()
        else:
            st.error("You can not delete book, if you can not solve simple math.")

if "books" not in st.session_state:
    st.session_state["books"] = []
if st.button("🚀 Load test books"):
    test_data = [
        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "price": 15.0},
        {"title": "1984", "author": "George Orwell", "price": 12.0},
        {"title": "Harry Potter", "author": "J.K. Rowling", "price": 25.0},
        {"title": "Dune", "author": "Frank Herbert", "price": 20.0},
        {"title": "The Witcher", "author": "Andrzej Sapkowski", "price": 18.0}
    ]
    st.session_state["books"].extend(test_data)
    st.success("Test books added!")
    st.rerun()
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
        st.success("The book has been added successfully!")
        st.balloons()
    else:
        st.warning("Please fill in all fields.")

if st.button("Show all books"):
    if len(st.session_state["books"]) == 0:
        st.write("No books added yet.")
    else:
        for book in st.session_state["books"]:
            st.write("Title:", book["title"])
            st.write("Author:", book["author"])
            st.write("Price:", book["price"])
            st.write("----------------------------")

st.header("🔍 Search by author")
search_author = st.text_input("Enter author's name")
if st.button("Search by author"):
    found = False
    for book in st.session_state["books"]:
        if search_author.lower() in book["author"].lower():
            st.write(book)
            found = True
    if found == False:
        st.write("No books from this author were found.")

st.header("📖 Search by title")
search_title = st.text_input("Enter book title")
if st.button("Search by title"):
    found = False
    for book in st.session_state["books"]:
        if book["title"].lower() == search_title.lower():
            st.write(book)
            found = True
    if found == False:
        st.write("No books with this title were found.")

if st.button("Show the cheapest book"):
    if len(st.session_state["books"]) == 0:
        st.write("No books available.")
    else:
        cheapest = min(st.session_state["books"], key=lambda x: x["price"])
        st.write("The cheapest book is:", cheapest)
st.header("Delete books")
search_delete = st.text_input("Enter book author or title")
math_check = st.number_input("Solve 5 + 15 to confirm deletion", value=0)

if st.button("Start search for deleting books"):
    found_delete = False
    for book in st.session_state["books"][:]:
        if search_delete.lower() in book["author"].lower() or search_delete.lower() in book["title"].lower():
            found_delete = True
            show_scary_popup(book, math_check)
            break
            
    if found_delete == False:
        st.write("No books matching your request were found.")
        
st.divider()
st.markdown("<h2 style='text-align: center; color: #FFD700;'>🎉 Congratulations! Your Library is ready! 📚</h2>", unsafe_allow_html=True)
