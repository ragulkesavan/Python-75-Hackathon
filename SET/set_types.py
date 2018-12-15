set1=set([1,2,3,"tallent","accurate"])
set2=frozenset([4,5,6,"frozen","set"])
print "normal set : ",set1
print "frozen set : ",set2
set1.add("new")
#set2.add("new")
print "normal set after adding: ",set1

,,,
OUTPUT:
normal set :  set(['tallent', 1, 2, 3, 'accurate'])
frozen set :  frozenset(['frozen', 'set', 4, 5, 6])
normal set after adding:  set([1, 2, 3, 'accurate', 'new', 'tallent'])
,,,
