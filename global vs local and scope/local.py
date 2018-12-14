#Using local variable in same name of global variable
def func():
     x=10 #local variable scope is within this function
     print "inside function func x = ",x

x=int(input("enter a number x ="))#global variable 
print "value entered in global scope x=",x
func()
print "value entered in global scope after function call x=",x#since only global variable have scope it gets printed

'''
OUTPUT:
enter a number x =20
value entered in global scope x=20
inside function func x = 10
value entered in global scope after function call x=20
'''
