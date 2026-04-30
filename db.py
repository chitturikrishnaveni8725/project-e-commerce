import mysql.connector
class DB:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Krishnasri@#8725",
            database="ecommerce"
                
        )
        self.cur=self.conn.cursor()
# print("db connected successfully!")
        
    def commit(self):
        self.conn.commit()      
    def close(self):
        self.conn.close()     