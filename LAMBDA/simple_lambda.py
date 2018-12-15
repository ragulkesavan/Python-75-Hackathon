g=lambda x,y:x>y
l=lambda x,y:x<y
e=lambda x,y:x==y

print "statement : 3 greater than 2 : ",g(3,2)
print "statement : 2 greater than 3 : ",g(3,2)
print "statement : 2 lesser  than 2 : ",l(2,3)
print "statement : 3 lesser  than 2 : ",l(3,2)
print "statement : 3  equals  to  2 : ",e(3,2)
print "statement : 3 greater than 3 : ",e(3,3)

'''
OUTPUT:
statement : 3 greater than 2 :  True
statement : 2 greater than 3 :  True
statement : 2 lesser  than 2 :  True
statement : 3 lesser  than 2 :  False
statement : 3  equals  to  2 :  False
statement : 3 greater than 3 :  True
'''
