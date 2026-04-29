

import mysql.connector

import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="sms_user",
        password="1234",
        database="SMS_"
    )
    
print("database connected successfully")

# Create table    
def create_table():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            course VARCHAR(100)
        )
    """)

    conn.commit()
    conn.close()

# Add student
def add_student(name, age, course):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)",
        (name, age, course)
    )

    conn.commit()
    conn.close()

# View students
def get_students():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    data = cur.fetchall()

    conn.close()
    return data

# Update student
def update_student(id, name, age, course):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        UPDATE students
        SET name=%s, age=%s, course=%s
        WHERE id=%s
    """, (name, age, course, id))

    conn.commit()
    conn.close()

# Delete student
def delete_student(id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE id=%s", (id,))

    conn.commit()
    conn.close()





