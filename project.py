import streamlit as st
import sql.connector
import pandas as pd


db=mysql.connector.connect(
host="localhost",
user="root",
password="Krishnasri@#8725",     
database="job_portal"
)
curobj=db.cursor()
print("db connected successfully!")
