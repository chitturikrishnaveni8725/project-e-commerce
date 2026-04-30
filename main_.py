from db import DB
from user import User
from product import Product
from orders import Order

db = DB()

u = User(db)
p = Product(db)
o = Order(db)

current_user = None

while True:
    print("""
    1. Signup
    2. Login
    3. Add Product
    4. View Products
    5. Place Order
    6. Cancel Order
    7. View Orders
    8. Exit
    """)

    choice = int(input("Enter option: "))

    if choice == 1:
        name = input("Name: ")
        email = input("Email: ")
        password = input("Password: ")
        u.signup(name, email, password)

    elif choice == 2:
        email = input("Email: ")
        password = input("Password: ")
        current_user = u.login(email, password)

    elif choice == 3:
        name = input("Product name: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        p.add_product(name, price, stock)

    elif choice == 4:
        p.view_products()

    elif choice == 5:
        if current_user:
            product_id = int(input("Product ID: "))
            qty = int(input("Quantity: "))
            o.place_order(current_user[0], product_id, qty)
        else:
            print("Login first")

    elif choice == 6:
        order_id = int(input("Order ID: "))
        o.cancel_order(order_id)

    elif choice == 7:
        if current_user:
            o.view_orders(current_user[0])
        else:
            print("Login first")

    elif choice == 8:
        break

db.close()