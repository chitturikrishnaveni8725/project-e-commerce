
# from db import DB

class User:
    def __init__(self,db):
        self.db=db
    def signup(self,name,email,password):
        try:
            self.db.cur.execute(
                
                
                "insert into users(name,email,password)values(%s,%s,%s)",
                (name, email, password)
            )    
            self.db.commit()
            print("sign up successfully")
        except:
            print("email already exists") 
    
    def login(self,email,password):
        self.db.cur.execute(
            "select * from users where email=%s and password=%s",
            (email,password)   
        )          
        user=self.db.cur.fetchone()
        if user:
            print("Login successfully")
            return user
        else:
            print("Invalid credentials")   
            return None 
# if __name__ == "__main__":
#     db = DB()
#     u = User(db)

#     print("\n--- USER TEST ---")

#     name = input("Enter name: ")
#     email = input("Enter email: ")
#     password = input("Enter password: ")

#     u.signup(name, email, password)

#     print("\nLOGIN TEST")
#     email = input("Enter login email: ")
#     password = input("Enter login password: ")

#     user = u.login(email, password)
#     print("Returned user:", user)

#     db.close()        
        
        
        