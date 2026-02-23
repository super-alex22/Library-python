import streamlit as st
st.title("My mini-library app")
if "books" not in st.session_state:
    st.session_state=[]
    st.header("Add book")
    title = st.text_input("Heading")
    author = st.text_input("Author")
    price = st.number_input("Price", min_value=0.0)
    if st.button("Add book"):
        book = {
            "title":title,
            "author":author,
            "price":price
        }
        st.session_state.books.append(book)
        st.success("The book has been added succesfully.")
if st.button("Show all books"):
    if len(st.session_state.books)==0:
        st.write("No books were added")
    else:
        for book in st.session_state.books:
            st.write("Title", book["title"])
            st.write("Author", book["author"])
            st.write("Price", book["price"])
            st.write("-------------------")

st.header("Search by author")
search_author = st.text_input("ENter author's name")
if st.button("Search by author"):
    found = False
    for book in st.session_state.books:
        if book["author"] == search_author:
            st.write(book)
            found = True
        if found == False:
            st.write("No books from this author were found")

st.header("Search by heading")
search_heading = st.text_input("ENter heading")
if st.button("Search by heading"):
    found = False
    for book in st.session_state.books:
        if book["heading"] == search_heading:
            st.write(book)
            found = True
        if found == False:
            st.write("No books from this author were found")
if st.button("Show the cheapest book"):
    if len(st.session_state.books) == 0:
        st.write("There are no such books")
    else:
        cheapest = st.session_state.books[0]
        for book in st.session_state.books:
            if book["price"] < cheapest["price"]:
                cheapest = book
        st.write("The cheapest books is {0}", cheapest)
