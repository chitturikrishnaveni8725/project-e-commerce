import streamlit as st
import database as db

db.create_table()

st.title("Student Management System (MySQL + Streamlit)")

menu = ["Add Student", "View Students", "Update Student", "Delete Student"]
choice = st.sidebar.selectbox("Menu", menu)


if choice == "Add Student":
    st.subheader("Add Student")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    course = st.text_input("Course")

    if st.button("Add"):
        db.add_student(name, age, course)
        st.success("Student Added!")


elif choice == "View Students":
    st.subheader("All Students")

    data = db.get_students()

    for row in data:
        st.write(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]}")

elif choice == "Update Student":
    st.subheader("Update Student")

    id = st.number_input("ID", min_value=1)
    name = st.text_input("New Name")
    age = st.number_input("New Age", min_value=1, max_value=100)
    course = st.text_input("New Course")

    if st.button("Update"):
        db.update_student(id, name, age, course)
        st.success("Updated!")

elif choice == "Delete Student":
    st.subheader("Delete Student")

    id = st.number_input("ID to delete", min_value=1)

    if st.button("Delete"):
        db.delete_student(id)
        st.warning("Deleted!")