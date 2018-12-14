#CLASS AND OBJECT
class org:#DEFINITION OF CLASS
    l=[]
    def order(self):
        name=input("enter the name of product : ")
        quantity=int(input("enter the quantity of product : "))
        address=input("enter delivery address :")
        self.l.append([name,quantity,address])
    def display_orders(self):
        for i in self.l:
            print i
#CREATING OBJECT FOR CLASS org
amazon=org()
#CALLING METHOD OF THE OBJECT
amazon.order()
amazon.order()
#CALLING METHOD OF CLASS
amazon.display_orders()

'''
INPUT:
"m1 note 4"
1
"tce mens hostel madurai"
"m1 note 5 pro"
1
"tce womens hostel madurai"
OUTPUT:
['m1 note 4', 1, 'tce mens hostel madurai']
['m1 note 5 pro', 1, 'tce womens hostel madurai']
'''
