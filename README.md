📘 E-Commerce System (Python + MySQL + OOP)
🔷 Project Overview

This project is a console-based e-commerce application developed using Python and MySQL, following Object-Oriented Programming (OOP) principles.

The system allows users to:

Register and login
Add and view products
Place and cancel orders
Track their order history

It is designed with modular architecture, where each functionality (User, Product, Order, Database) is separated into different files.
🎯 Project Objective
To implement real-world e-commerce workflow
To practice OOP concepts
To integrate Python with MySQL
To handle data consistency (stock & orders)

📂 Project Structure
db.py        → Database connection
user.py      → User management
product.py   → Product management
orders.py    → Order management
main.py      → Application controller

📄 1. db.py (Database Layer)

Establishes connection to MySQL database.
Creates cursor for executing SQL queries.
Provides commit() to save changes.
Provides close() to terminate connection.
Acts as a shared resource across all modules.

👤 2. user.py (User Module)

Handles user registration and login.
Stores user data in database.
Validates login credentials.
Returns user details after login.
Handles duplicate email errors

📦 3. product.py (Product Module)

Manages product-related operations.
Adds new products to database.
Displays all available products.
Maintains product price and stock.
Uses DB connection for queries.


🛒 4. orders.py (Order Module)

Handles placing and cancelling orders.
Validates product availability.
Updates stock after order.
Restores stock on cancellation.
Displays user-specific orders.


🧭 5. main.py (Controller / Entry Point)

Acts as main program controller.
Connects all modules together.
Provides menu-driven interface.
Handles user input and flow.
Maintains logged-in session.
