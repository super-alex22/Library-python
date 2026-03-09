import streamlit as st

st.title("My Library App")

if "books" not in st.session_state:
    st.session_state["books"] = []

# ==========================================
# ➕ Add a book
# ==========================================
st.header("➕ Add a book")
title = st.text_input("Title", key="input_title")
author = st.text_input("Author", key="input_author")
price = st.number_input("Price", min_value=0.0, step=0.01)

if st.button("Add the book"):
    if title.strip() and author.strip():
        book = {
            "title": title,
            "author": author,
            "price": price
        }
        st.session_state["books"].append(book)
        st.success(f"Success! '{title}' is now on the shelf.")
    else:
        st.warning("Please enter both title and author. No 'anonymous' masterpieces allowed!")

# ==========================================
# 📚 Show all books
# ==========================================
st.divider()
if st.button("Show all books"):
    books = st.session_state["books"]
    if not books:
        st.info("The library is empty. Go buy some books!")
    else:
        for b in books:
            st.write(f"📖 **{b['title']}** | {b['author']} | ${b['price']}")

# ==========================================
# 🔍 Search
# ==========================================
st.header("🔍 Search")
search_query = st.text_input("Search by author or title")
if st.button("Run Search"):
    results = [
        b for b in st.session_state["books"] 
        if search_query.lower() in b["author"].lower() or search_query.lower() in b["title"].lower()
    ]
    if results:
        for res in results:
            st.write(f"✅ Found: {res}")
    else:
        st.error("Nothing found. Check your spelling!")

# ==========================================
# 💰 Statistics
# ==========================================
if st.button("Show the cheapest book"):
    books = st.session_state["books"]
    if not books:
        st.write("Nothing to compare.")
    else:
        cheapest = min(books, key=lambda x: x["price"])
        st.balloons() # Немного праздника при поиске выгоды!
        st.write(f"The cheapest book is: **{cheapest['title']}** for ${cheapest['price']}")
