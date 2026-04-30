# import mysql.connector
# import pandas as pd
# import streamlit as st


# db=mysql.connector.connect(
# host="localhost",
# user="root",
# password="Krishnasri@#8725",
# database="ems",
# auth_plugin="mysql_native_password"
# )

# print(db)
# print("db connected succesfully")
# curobj=db.cursor()


# curobj.execute  ("""

# create table if not exists student_(
#      id int primary key auto_increment,
#                  name varchar(30)  not null,
#                  age int ,
#                  place varchar(30) not null,
#                  email varchar(50) not null,
#                  password varchar(30) not null

                
#                  )

# """)
# print("table created successfully!")



# st.title("Student Management System")
# st.info("Enter student deatils carefully")


# choose=st.sidebar.selectbox("choose option ",["ADD","VIEW","DELETE","UPDATE"])
# if choose=="ADD":
#     name=st.text_input("Enter your name here:")
#     age=int(st.number_input("Enter your age here:",step=1))
#     place=st.text_input("Enter your  city here:")
#     email=st.text_input("Enter your email here:")
#     password=st.text_input("Enter your password here:",type="password")
#     address=st.text_area("Enter your address here:",placeholder="Address")
#     query="insert into student_(name,age,place,email,password)values(%s,%s,%s,%s,%s)"
#     values=[name,age,place,email,password]
#     curobj.execute(query,values)
#     db.commit()
#     if st.button("submit"):
#         st.success(f"{name} added  your details successfully")

# if choose=="VIEW":
#     curobj.execute("select * from student_")
#     records=curobj.fetchall()
#     st.write("student details")
#     st.dataframe(records)
#     st.success("view details succesfully!")    

# if choose=="DELETE":
#     name=st.text_input("enter name")
#     query="delete from  student_ where name=%s"
#     value=[name,]
#     curobj.execute(query,value)
#     db.commit()
#     if st.button("submit"):
#         st.success("student delete successfully")


# # if choose=="DELETE":
# #     if st.button("delete all data"):
# #         curobj.execute("delete from student_") 
# #         db.commit()
# #         st.success("all data removed successfully!")
# #         st.rerun()


# if choose=="UPDATE":
#     name=st.text_input("enter your name:")
#     age=st.number_input("enter your age:")
#     id=st.text_input("enter  your id :")
#     query="update student_ set name=%s ,age=%s  where id=%s"
#     values=[name,age,id]
#     curobj.execute(query,values)
#     db.commit()
#     st.write(f"{name} your details updated successfully!..")
#     st.sucess("updated successfully")



import mysql.connector
import streamlit as st

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Krishnasri@#8725",
    database="ems",
    auth_plugin="mysql_native_password"
)

curobj = db.cursor()

curobj.execute("""
CREATE TABLE IF NOT EXISTS student_(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    age INT,
    place VARCHAR(30),
    email VARCHAR(50),
    password VARCHAR(30)
)
""")

st.title("Student Management System")
st.info("Enter student details carefully")

choose = st.sidebar.selectbox("Choose option", ["ADD", "VIEW", "DELETE", "UPDATE","DELETEALL"])

# ---------------- ADD ----------------
if choose == "ADD":
    name = st.text_input("Enter name")
    age = st.number_input("Enter age", step=1)
    place = st.text_input("Enter city")
    email = st.text_input("Enter email")
    password = st.text_input("Enter password", type="password")

    if st.button("Submit"):
        query = "INSERT INTO student_(name,age,place,email,password) VALUES (%s,%s,%s,%s,%s)"
        values = (name, age, place, email, password)
        curobj.execute(query, values)
        db.commit()
        st.success(f"{name} added successfully!")

# ---------------- VIEW ----------------
elif choose == "VIEW":
    curobj.execute("SELECT * FROM student_")
    records = curobj.fetchall()
    st.dataframe(records)

# ---------------- DELETE ----------------
elif choose == "DELETE":
    name = st.text_input("Enter name to delete")

    if st.button("Delete"):
        query = "DELETE FROM student_ WHERE name=%s"
        curobj.execute(query, (name,))
        db.commit()
        st.success("Student deleted successfully!")
elif choose == "DELETE ALL":
    if st.button("delete all"):
        records=curobj.fetchall()
        curobj.execute("drop  table stud")
        db.commit()
        st.success("deleted students successfully")



# ---------------- UPDATE ----------------
elif choose == "UPDATE":
    id = st.number_input("Enter ID", step=1)
    name = st.text_input("Enter new name")
    age = st.number_input("Enter new age", step=1)

    if st.button("Update"):
        query = "UPDATE student_ SET name=%s, age=%s WHERE id=%s"
        curobj.execute(query, (name, age, id))
        db.commit()
        st.success("Updated successfully!")



