
import json

file_name = "students.json"

#  Load data
def load_data():
    try:
        with open(file_name, "r") as f:      
            return json.load(f)
    except:
        return []

#  Save data
def dump_data(data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

#  Add Student 
def add_student():
    allstuds = load_data()

    name = input("Enter name: ")
    age = int(input("Enter age: "))

   
    if len(allstuds) == 0:
        new_id = 1
    else:
        new_id = allstuds[-1]["id"] + 1

    new_data = {"id": new_id, "name": name, "age": age}
    allstuds.append(new_data)

    dump_data(allstuds)
    print(" Student added successfully!")

#  View Students
def view_students():
    allstuds = load_data()
    if not allstuds:
        print("No students found.")
        return

    for i in allstuds:
        print(i["id"], i["name"], i["age"])

#  Search Student
def search_student():
    allstuds = load_data()

    choice = input("Search by (1) ID or (2) Name: ")

    if choice == "1":
        sid = int(input("Enter ID: "))
        for s in allstuds:
            if s["id"] == sid:
                print(s)
                return
        print(" Student not found")

    elif choice == "2":
        name = input("Enter name: ").lower()
        found = False
        for s in allstuds:                      
            if name in s["name"].lower():
                print(s)
                found = True
        if not found:
            print(" No matching student")

#  Update Student
def update_student():
    allstuds = load_data()
    view_students()

    sid = int(input("Enter ID to update: "))

    for s in allstuds:
        if s["id"] == sid:
            s["name"] = input("Enter new name: ")
            s["age"] = int(input("Enter new age: "))
            dump_data(allstuds)
            print(" Updated successfully!")
            return

    print(" Student not found")

#  Delete Student
def delete_student():
    allstuds = load_data()
    view_students()

    sid = int(input("Enter ID to delete: "))

    for s in allstuds:
        if s["id"] == sid:
            allstuds.remove(s)
            dump_data(allstuds)
            print(" Deleted successfully!")
            return

    print(" Student not found")

#  Menu
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        break
    else:
        print("Invalid choice")