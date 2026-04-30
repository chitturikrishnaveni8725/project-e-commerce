# import json






import json

file_name="students.json"
data=[{"name": "akhil", "age": 29}, {"name": "srinu", "age": 22}]
data=[{"name":"sri","age":20},{"name":"ram","age":23}]
print(type(data))
c=json.dumps(data)
print(type(c))
s=json.loads(c)
print(type(s))

def load_data():
        try:
            with open(file_name,"r") as f:
                  
                return json.load(f)
        except:
               return []            
             

def dump_data(data):
            with open(file_name,"w") as f:
                  json.dump(data,f,indent=4)

def add_student():
       allstudents=load_data()   
       name=input("Enter yout name here:-") 
       age=int(input("Enter you age here"))  
       new_data={"name":name,"age":age}   
       allstudents.append(new_data)
       dump_data(allstudents) 
       print("student added successfully!..")

add_student()



def view_student():
       allstudents=load_data()
       for i in allstudents:
              print(i)
              dump_data(i)
              print("stduent viwed successsfully")

view_student()

def student_updates():
       allstduents=load_data
       view_student()
       name=input("enter your name:-- ")
       age=input("enter your age:--")

       allstduents.update({"name":name,"age":age})
       dump_data(allstduents)
       print("stduent updated successfully")
            

               
                  
                              
                  
                  
                  
                 
                
  
      

