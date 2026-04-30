# from db import DB


class Product:
    def __init__(self,db):
        self.db=db
        
    def add_product(self,name,price,stock):
        self.db.cur.execute(
            
            
            "Insert into products(name,price,stock)values(%s,%s,%s)",
            (name,price,stock)
        )   
        self.db.commit()
        print("producut added successfully!")
    def view_products(self):
        self.db.cur.execute("select * from products")
        for row in self.db.cur.fetchall():
             print(row)
        # products_=self.db.cur.fetchall()
        # print("\n product list----")
        # for p in products_:
        #     print(f"Id:{p[0] }| Name: {p[1]} | price: {p[2]} | Stock:{p[3]}")
        
              


# ✅ TEST RUN SECTION
# if __name__ == "__main__":
#     db = DB()
#     obj = Product(db)

#     name = input("Enter product name: ")
#     price = float(input("Enter price: "))
#     stock = int(input("Enter stock: "))

#     obj.add_product(name, price, stock)

#     print("\nShowing products...\n")
#     obj.view_products()

#     db.close()
        