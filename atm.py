# import streamlit as st
# st.title("STUDENT  MANAGEMNET SYSTEM")
# st.header("enter your details here")

# # st.form("enter your deatils")
# # name=st.text_input("enter your name",max_chars=20)
# # age=st.text_input("enter your age")
# # email=st.text_input("enter yout email here")
# # password=st.text_input("enter password", type="password")
# # st.radio("choose gender",["male","female","none"])
# # st.checkbox("I agree all terms and conditions")

# # st.write("seleted carefully")
# # st.button("submit")

# # st.success("student details submitted successfully")


# # if st.button("submit"):
# #     if name=="" :
# #         st.warning("You should  fill your name ")
# #     elif password<8:
# #         st.warning("you should enter your age ")
# #     elif age<18:
# #         st.error("age should be 18+")    
# #     elif  '@mail' not in email:
# #         st.warning("please enter valid emial with contain @gamil")  
# #     else:
# #         st.success("login successfully")   
        


# data=st.dataframe({"name",["krishnasri","ram"]}
#                   )
# st.line_chart(data)

import streamlit as st
import pandas as pd


df = pd.DataFrame({
    "name": ["krishnasri", "ram","sai","janani"],
    "marks": [80, 90,100,200] 
})

st.dataframe(df)

st.bar_chart(df.set_index("name"))