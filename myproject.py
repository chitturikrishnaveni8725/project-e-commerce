import streamlit as st
import pandas as pd

st.title("hello welcome to my page")
# st.header("krishnasri chitturi")
# st.subheader("hi heyyy")
# st.sidebar.selectbox("menu",["Home","About"])

# name=st.text_input("Enter your name here")
# age=st.number_input("Enter your age here")
# password=st.text_input("password",type="password")

# st.info("if you click the submit button you should be enter the name and  age ")                 

# if st.button("Submit"):
#     if name=="" or age==0 or password>8:
#             st.warning("you should enter here")
#     elif age<18:
#           st.error("age must be 18>")   
#     else:
#           st.success("You are login here") 



name=st.text_input("enter you name here")
age=int(st.number_input("enter your age here :",step=1))
email=st.text_input("enter your email here:")
pwd=st.text_input("Enter your Password her",type="password")
if st.button("Add"):
      data=pd.DataFrame( {"Name":[name],
                          "Age":[age],
                          "Email":[email],
                          "Password":[pwd]
      }
      )
      st.success("Details Added Successfully")
      st.dataframe(data)  
st.sidebar.selectbox("choose option here:--",["Add","View","Update","Delete"])
st.info("Please fill the deatils carefully")
if st.button("submit"):
      if age<18:
            st.error("age should be 18 +")
      elif name=="" or pwd=="" or email=="":
            st.warning("inputs should be fill")  
      else:
            st.sucess("successfully added")      



  
