import mysql.connector
db=mysql.connector.connect(
host="localhost",
user="root",
password="Krishnasri@#8725",
database="invert"

)
print(db)
print("db connected succesfully")
curobj=db.cursor()


# 3. Simple Inventory System
# Products table (id, name, quantity, price)
# Python:
# Add product
# Update stock
# Show low stock items


curobj.execute("""
create table if not exists invertory(
            id int auto_increment primary key,
            name varchar(50) not null,
            quantity int ,
            price decimal (10,2))
""")
db.commit()
# print("table created successfully")


# add product
def func_add():
    name=input("enter your name here:--")
    quantity=int(input("enter your quantity here:--"))
    price=float(input("Enter price here:--"))
    query="insert into invertory(name,quantity,price) values(%s,%s,%s)"
    values=[name,quantity,price]
    curobj.execute(query,values)
    print("product details successfully!..")
    db.commit()
# func_add()   

def func_update():
    quantity=int(input("enter quantity here:--"))
    price=float(input("Enter price here:-- "))
    id=int(input("enter id here:---"))
    query="update invertory set quantity=%s, price=%s where id=%s"
    values=(quantity,price,id)
    curobj.execute(query,values)
    print("details updated successfully!..")
    db.commit()
# func_update()    


def func_view():
    curobj.execute("select * from invertory")
    records=curobj.fetchall()
    for i in records:
        id,name,quantity,price =i
        print(f"{id}||{name}||{quantity} ||{float(price)}")
# func_view()  


def lowstock_fun():
    curobj.execute("select * from invertory where quantity<5")
    records_=curobj.fetchall()
    print("\n   Viwe Low Stock Items ")
    for i in records_:
        id, name,quantity,price=i
        print(f"{id}  || {name} || {quantity} || {price:.2f}")
# lowstock_fun()     
        
while True:
    print("\n \n Welcome to my inventory store:")  
    print("""
    1.Add product
    2.View Product
    3.Update Product
    4.Low Stock products
    5.Exit      
     """  )
    try:
        choice=int(input("Enter your choice here:---"))
    except ValueError:
        print("please enter only number please !")   
        continue   
    if choice==1:
        func_add()  
    elif choice==2: 
        func_view() 
    elif choice==3: 
         func_update()  
    elif choice==4:
        lowstock_fun()  
    else:
        print("Bye") 
        break     

  

        




        

