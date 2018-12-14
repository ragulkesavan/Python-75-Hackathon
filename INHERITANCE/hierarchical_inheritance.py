class orders:#DEFINITION PARENT CLASS OF CLASS
    l=[]
    def order(self):
        product_name=input("enter the name of product : ")
        quantity=int(input("enter the quantity of product : "))
        address=input("enter delivery address :")
        self.l.append([product_name,quantity,address])
    def display_orders(self):
        for i in self.l:
            print i
class customer(orders): 
    def get_cust(self):
        cus_name=input("cust name : ")
        self.order()
class vendor(orders):
    def get_vendor(self):
        vend_name=input("vendor name : ")
        self.display_orders()
c=customer()
c.get_cust()
v=vendor()
v.get_vendor()
