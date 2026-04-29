from database_ import db,curobj
# from login import Login

class Register_:
    
    def __init__(self,n,ac_num,fst_bal):
        queryTableCreation="""
        create table if not exists users(
            customer_id int primary key auto_increment,
            name varchar(50) not null,
            acc_num varchar(16) unique not null,
            balance decimal(10,2) not null,
            password varchar(16) not null
                
        )
        """
        curobj.execute(queryTableCreation)
        print("table created successfully")
        p=input("enter password here:--")
        cp_p=input("Enter a password to conform:--")
        if p==cp_p:
            query="insert into users(name,acc_num,balance,password)values(%s,%s,%s,%s)"
            values=(n,ac_num,fst_bal,p)
            curobj.execute(query,values)
            db.commit()
            print("student registered successfully")
            
name=input("Enter name here:--")  
acc=input("Enter your account number here:--")   
bal=input("Enter balance here:--")   
Register_(name,acc,bal)

        
