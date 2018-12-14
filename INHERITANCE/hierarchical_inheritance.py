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

'''
SAMPLE I/O:
cust name : "cust_1"
enter the name of product : "mi note 4" 
enter the quantity of product : 1
enter delivery address : "tce mens hostel"
vendor name : "vend_1"
['mi note 4', 1, 'tce mens hostel']
'''
