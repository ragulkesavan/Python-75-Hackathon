l=[]
def get_order(cust_name):
  global l 
  product_name=input("enter the name of product : ")
  quantity=int(input("enter the quantity of product : "))
  address=input("enter delivery address :")
  l.append([cust_name,product_name,quantity,address])
  
  
def display_orders():
    for i in l:
        print(i)
        

def get_cust():
    cus_name=input("cust name : ")
    get_order(cus_name)
    
def get_vendor():
    vend_name=input("vendor name : ")
    display_orders()
