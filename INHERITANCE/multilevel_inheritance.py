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
class user(orders): 
    def get_cust(self):
        cus_name=input("cust name : ")
    def get_vendor(self):
        vend_name=input("vendor name : ")

class amazon(user):
    def __init__(self):
        print "customer->1 \nvendor->2"
        n=int(input("give choice : "))
        if n==1:
            self.get_cust()
            self.order()
        elif n==2:
            self.get_vendor()
            self.display_orders()
        else :
            print "wrong choice"
a=amazon()
a.__init__()
