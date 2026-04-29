
from database_ import curobj,db


class Dashboard:
    def __init__(self,i):
        print("dashboard")
        print(i)
        
        
        while True:
            print("""
            explore customer features -HDFC BANK
            1.withdraw
            2.deposit
            3.check_bal
            4.exit
                  """)
            
            o=int(input("enter option: "))
            
            
            if o==1:
                
                p=input("Enter your password to withdraw the amount:")
                a=int(input("Enter amount to draw here:---"))
                
                def withdraw(incomingp,withdrawAmt):
                    nonlocal i
                    
                    
                    if incomingp==i[-1]:
                        if withdrawAmt<=0:
                            print("Enter valid amount")
                            return None
                        
                        if withdrawAmt<=float(i[3]):
                                i=list(i)  
                                i[3] = float(i[3]) - withdrawAmt
                                return i[3]
                        else:
                            
                            print(f"insufficient funds:- your balnce is{i[3]}")  
                            return None    
                    else:
                        print("wrong pin entered")
                        return None
                rem_bal=withdraw(p,a)
                if rem_bal is not None:
                    q="update users set balance=%s where acc_num=%s and password=%s"
                
                    d=(rem_bal, i[2], p)
                    curobj.execute(q,d) 
                    db.commit()   
                    print(f"Remaining bal is  {rem_bal} and withdraw amount is {a}" )   
                else:
                    print("Transcation failed")     
            elif o==2:
                print("deposit feature")  
               

                acc_num = input("Enter account number: ").strip()
                deposit_money = int(input("Enter amount to deposit: "))
                pwd = input("Enter password: ").strip()

                if acc_num == i[2] and pwd == i[-1]:
                    if deposit_money <= 0:
                        print("Enter valid amount")
                    else:
                        new_balance = float(i[3]) + deposit_money

                        q = "UPDATE users SET balance=%s WHERE acc_num=%s AND password=%s"
                        d = (new_balance, acc_num, pwd)

                        curobj.execute(q, d)
                        db.commit()

                        i = list(i)   # update local data also
                        i[3] = new_balance

                        print(f"Deposited {deposit_money} successfully")
                        print(f"Updated balance: {new_balance}")
                else:
                    print("Invalid account number or password")
                    
                
                
            elif o==3:
                p=input("enter password to check the balance:--")
                def check_bal(incomingp):
                    if incomingp==i[-1]:
                        return i[3]
                    else:
                        print("Enter proper pin to proceed further")
                bal=check_bal(p)
                if bal is not None:
                    print(f"main bal is {bal}")    
                
            elif o==4:
                print("Thankyou!")   
                    
                  
                           