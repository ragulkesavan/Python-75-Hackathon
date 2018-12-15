s=set([1,2,3,4,5])
t=set([1,3,5])
if t.issubset(s):
    print t," is subset of ",s
elif s.issubset(t):
    print s,"is subset of ",t
    
'''
OUTPUT:
set([1, 3, 5])  is subset of  set([1, 2, 3, 4, 5])
'''
