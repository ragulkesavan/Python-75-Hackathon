#empty list
l1=[]
print "empty list",l1

#list creation 
l=[1,2,3,4,5,6,"talent","torento","accurate"]
print "list created l : ",l

#length of list using len()
print "lenght of the list is ",len(l)

#check whether the element is in list by using in operator
if "talent" in l:
    print "talent in list ? yes"
else :
    print "talent in list ? no"

#adding elements to list using append()
print "list l : ",l
l.append("canada")
print "list l after appending canada: ",l

#adding elements to list using insert()
print "list l : ",l
l.insert(1,"one")
print "inserting one at index 1 list l : ",l

#remove an element using remove method
l.remove("torento")
print "list l after removing torento : ",l

#removing element using index
del l[5]
print "list l after del 5 indexed element: ",l

#finding the no of times the element occur in count()
print "no of times 1 occurs in l is ",l.count(1)

#finding the index of a element
print "index of the element accurate is : ",l.index("accurate")

#reversing the list
l.reverse()
print "list l after reversing: ",l

#sorting the list
l.sort()
print "list l aftersorting : ",l

#adding all the elements in a list to another using extend function
l2=[9,8,10,11]
l.extend(l2)
print "list l after appending l2 list: ",l

#del a list
del l


'''
OUTPUT:

empty list []
list created l :  [1, 2, 3, 4, 5, 6, 'talent', 'torento', 'accurate']
lenght of the list is  9
talent in list ? yes
list l :  [1, 2, 3, 4, 5, 6, 'talent', 'torento', 'accurate']
list l after appending canada:  [1, 2, 3, 4, 5, 6, 'talent', 'torento', 'accurate', 'canada']
list l :  [1, 2, 3, 4, 5, 6, 'talent', 'torento', 'accurate', 'canada']
inserting one at index 1 list l :  [1, 'one', 2, 3, 4, 5, 6, 'talent', 'torento', 'accurate', 'canada']
list l after removing torento :  [1, 'one', 2, 3, 4, 5, 6, 'talent', 'accurate', 'canada']
list l after del 5 indexed element:  [1, 'one', 2, 3, 4, 6, 'talent', 'accurate', 'canada']
no of times 1 occurs in l is  1
index of the element accurate is :  7
list l after reversing:  ['canada', 'accurate', 'talent', 6, 4, 3, 2, 'one', 1]
list l aftersorting :  [1, 2, 3, 4, 6, 'accurate', 'canada', 'one', 'talent']
list l after appending l2 list:  [1, 2, 3, 4, 6, 'accurate', 'canada', 'one', 'talent', 9, 8, 10, 11]'''
