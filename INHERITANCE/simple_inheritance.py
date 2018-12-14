class orders:#DEFINITION PARENT CLASS OF CLASS
    l=[]
    def order(self):
        name=input("enter the name of product : ")
        quantity=int(input("enter the quantity of product : "))
        address=input("enter delivery address :")
        self.l.append([name,quantity,address])
    def display_orders(self):
        for i in self.l:
            print i
class e_com_org(orders): #INHERITANCE OF orders(PARENT) class in e_com_org(CHILD) class
    def customer(self):
        cust_name=input("name : ")
        self.order()  #USING THE MEMBER OF PARENT customer can give order
    def vendor(self):
        vendor_name=input("enter name : ")
        self.display_orders() #vendor can see all orders recieved
amazon=e_com_org()
amazon.customer()
amazon.vendor()



'''
OUTPUT:
name : "CUST_1"
enter the name of product : "mi note 4"
enter the quantity of product : 1
enter delivery address : "tce mens hostel"
enter name : "vendor_1"
['mi note 4', 1, 'tce mens hostel']
'''
