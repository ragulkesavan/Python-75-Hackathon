#SCOPE USING NONLOCAL KEYWORD
x = 10#GLOBAL VARIABLE X
def outer():
    x=20#LOCAL VARIABLE X
    y=30#LOCAL VARIABLE Y
    print("outer func x before inner call:", x)
    print("outer func y before inner call:", y)
    def inner():
        nonlocal y#LOCAL VARIABLE Y REFERS TO ITS ABOVE LEVEL OUTER Y
        global x#REFERS GLOBAL X
        x=30#MAKS GLOBAL X TO 30
        y=40#MAKES LOCAL Y IN OUTER TO 40
        print("inner func x :", x)
        print("inner func y :", y)

    inner()
    print("outer func x after inner call:", x)
    print("outer func y after inner call:", y)
    
print("x before outer call:", x)
outer()
print("x after outer call:", x)

'''
OUTPUT:
x before outer call:10
outer func x before inner call:20
outer func y before inner call:30
inner func x :30
inner func y :30
outer func x after inner call:20
outer func y after inner call:40
x before outer call:30'''
