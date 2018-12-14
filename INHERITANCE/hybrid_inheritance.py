#MULTIPLE INHERITANCE
#When a child class inherits from multiple parent classes, it is called as multiple inheritance.

class orders:#DEFINITION PARENT CLASS
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
#DEFINITION PARENT CLASS 
    def get_cust(self):
        cus_name=input("cust name : ")
        self.order()
        
class vendor(orders):
#DEFINITION PARENT CLASS
    def get_vendor(self):
        vend_name=input("vendor name : ")
        self.display_orders()
        
class amazon(customer,vendor):
#DEFINITION CHILD CLASS -IT INHERITS MORE THEN 1 PARENT
    def __init__(self):
        print "customer->1 \nvendor->2"
        n=int(input("give choice : "))
        if n==1:
            self.get_cust()
        elif n==2:
            self.get_vendor()
        else :
            print "wrong choice"
a=amazon()
a.__init__()

'''
SAMPLE I/O:
customer->1 
vendor->2
give choice : 1
cust name : "cust_1"
enter the name of product : "mi note 4" 
enter the quantity of product : 1
enter delivery address : "tce mens hostel"
customer->1 
vendor->2
give choice : 2
vendor name : "vend_1"
['mi note 4', 1, 'tce mens hostel']
'''
