import mysql.connector

db=mysql.connector.connect(
    
  host="localhost",
  user="root",
  password="Krishnasri@#8725",
  database="student_db"  
    
)

print("database connected successfully!")
curobj=db.cursor()