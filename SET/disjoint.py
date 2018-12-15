s=set([1,2,3,4,5])
t=set([6,7,8,9,10])
u=set([1,2,6,7])
if s.isdisjoint(t):
    print s,t," are disjoint"
else :
    print s,t," are joining"
if s.isdisjoint(u): 
    print s,t," are disjoint"
else :
    print s,t," are having intersecting elements"
    
   
'''
OUTPUT:
set([1, 2, 3, 4, 5]) set([8, 9, 10, 6, 7])  are disjoint
set([1, 2, 3, 4, 5]) set([8, 9, 10, 6, 7])  are joining
'''
