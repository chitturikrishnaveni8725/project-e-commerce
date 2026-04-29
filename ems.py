
import mysql.connector
db=mysql.connector.connect(
host="localhost",
user="root",
password="Krishnasri@#8725",
database="sms"
)


print(db)
print("Connected sucessfully!")

cursor=db.cursor() # to run sql commnads we use cursor function
cursor.execute("""

create table if not exists employees(emp_id int primary key auto_increment,
               emp_name varchar(30)not null,
               city varchar(30) not null,
               department varchar(20) not null,
               age int,
               salary decimal(10,2) check(salary>0))


""")
print("Table created successfully!.....")
# inserting values 
def add_employee():
    emp_id=int(input("Enter your id:"))
    emp_name=input("Enter your name:")
    city=input("Enter your city:")
    department=input("Enter your department:")
    age=int(input("Enter your age:"))
    salary=input("Enter your salary:")
    query="insert into  employees(emp_id,emp_name,city,department,age,salary)values(%s,%s,%s,%s,%s,%s)"
    values=(emp_id,emp_name,city,department,age,salary)
    cursor.execute(query,values)
    print("Employee Details Added Succesfully!") 
    db.commit()    

def employee_view():
    cursor.execute("select * from employees")
    records=cursor.fetchall()
    # print("Employee details viewd successfully!")
    for i in records:
        emp_id,emp_name,city,department,age,salary=i
        print(emp_id,emp_name,city,department,age,float(salary))
        db.commit()


def employee_update():
    emp_name=input("Enter name:")
    salary=input("Enter salary:")
    emp_id=int(input("Enter id:"))
    query="update employees set emp_name=%s,salary=%s where emp_id=%s"
    values=(emp_name,salary,emp_id)
    cursor.execute(query,values)
    db.commit()
    print("Employee deatils updated successfully!")    

def employee_delete():
    emp_id=int(input("Enter id:"))
    query="delete from employees where emp_id=%s"
    value=(emp_id,)
    cursor.execute(query,value)
    db.commit()
    print("Employee record Deleted")
while True:
    print("\n------ Employee Management System------")
    choose=("1.add employee || 2. view employee || 3.update employee || 4.delete employee")
    print(choose)
    choice=input("Enter your choice here:")
    if choice=='1':
        add_employee()
    elif choice=='2':
        employee_view()
        print("Employee details viewd successfully!")
    elif choice=='3':
        employee_update()  
    elif choice=='4':
        employee_delete()  
        break
    else:
        print("invalid choice")











