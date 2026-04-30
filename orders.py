class Order():
    def __init__(self,db):
        
        self.db=db
        
    def place_order(self,user_id,product_id,qty):
        self.db.cur.execute("select price,stock from products where id=%s",
                            (product_id,))  
        product=self.db.cur.fetchone()
        
        
        if not product:
            print("Product Not found")
            return None
        price,stock=product  
        
        if stock<qty:
            print("not enough stock")
            return None
        total=price*qty
        
        self.db.cur.execute("insert into orders(user_id,product_id,quantity,total_price,status)values(%s,%s,%s,%s,%s)",
                          (user_id, product_id, qty, total, "Placed")             
                            
                            
                            )
        self.db.cur.execute(
            "UPDATE products SET stock=%s WHERE id=%s",
            (stock - qty, product_id)
        )
        self.db.commit()
        print("Order placed")
    def cancel_order(self, order_id):
        self.db.cur.execute("SELECT product_id, quantity FROM orders WHERE id=%s", (order_id,))
        order = self.db.cur.fetchone()  
        
        if not order:
            print("Order not found")
            return  
        product_id, qty = order
        self.db.cur.execute("SELECT stock FROM products WHERE id=%s", (product_id,))
        stock = self.db.cur.fetchone()[0]
        self.db.cur.execute(
            "UPDATE products SET stock=%s WHERE id=%s",
            (stock + qty, product_id)
        )
        self.db.cur.execute(
            "UPDATE orders SET status='Cancelled' WHERE id=%s",
            (order_id,)
        )
        self.db.commit()
        print("Order cancelled")
    def view_orders(self, user_id):
        self.db.cur.execute("SELECT * FROM orders WHERE user_id=%s", (user_id,))
        orders = self.db.cur.fetchall()
        for o in orders:
            print(o)    



                            
                            
                            
                            