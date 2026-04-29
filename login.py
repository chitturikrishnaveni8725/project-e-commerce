from database_ import db,curobj
class Login:
    def __init__(self,an,p):
        queryToFetchData="select * from users"
        curobj.execute(queryToFetchData)
        usersData=curobj.fetchall()
        found=False
       
            
        # for i in usersData:
        #     print(i)
        # print("users details send successfully")
        for i in usersData:
            if i[2]==an and i[4]==p:
                from dashboard import Dashboard
                Dashboard(i)
                found=True
                break
        if not found:
            
            print("Customer nor found with that details")
           
    
an=input("Enter your account number here:--").strip() 
ps=input("Enter your password here:--").strip() 
Login(an,ps)    
        
        
        
