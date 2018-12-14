def func():
    global x #global keyword makes global scope of x
    x=30#changes global x value
    print "IN FUNC() GLOBAL X IS CHANGED TO 30"
x=10
print "value entered in global scope x = ",x
func()
print "value entered in global scope after function call x=",x#since only global variable have scope it gets printed

'''
OUTPUT:
$python main.py
value entered in global scope x =  10
IN FUNC() GLOBAL X IS CHANGED TO 30
value entered in global scope after function call x= 30
'''
