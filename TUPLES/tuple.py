#tuples
'''TUPLES ARE UNCHANGABLE ORDERED COLLECTION OF DATA VALUES
   ONCE TUPLES ARE CREATED NEW VALUES CANNOT BE ADDED,EXISTING VALUES CANNOT BE 
   DELETED OR RE-ORDERED OR CHANGED
   TUPLES ARE REPRESENTED USING ROUND BRACES () INBETWEEN VALUES ARE SEPERATED BY COMMA 
   TUPLES ARE IMMUTABLE'''
   
#TUPLE CREATION
t=(1,2,3,4,5,"talent","accurate")

#ACCESSING TUPLES BY INDEXING
print "THE SECOND ELEMENT IN THE TUPLE IS : ",t[1]

#ACCESSING TUPLES BY INDEXING FORM LAST -indexing form last starts from -1 and goes as -2,-3
print "THE LAST ELEMENT IN THE TUPLE IS : ",t[-1]

#LENGTH OF TUPLE -len(t)
print "THE LENGTH OF THE TUPLE IS : ",len(t)

#count(x) in tuple -counts the no of times x occurs in tuple
print "THE TOTAL NUMBER OF TIMES GIVEN VALUE IS IN THE TUPLE : ",t.count(1)

#index(x) function in tuple -gives the index of the element x 
print "THE INDEX OF GIVEN VALUE IS IN THE TUPLE talent : ",t.index("talent")

#element present in tuple
if "accurate" in t:
    print "yes present"
else :
    print "no"
#for loop for tuple
for i in t:
    print i
#concatenation of tuple t[a:b]-creates new tuple from ath elemnt to b-1th element of t
print "sliced tuple : ",t[0:5]
#deletion of tuple
del(t)
 
'''
OUTPUT:
THE SECOND ELEMENT IN THE TUPLE IS :  2
THE LAST ELEMENT IN THE TUPLE IS :  accurate
THE LENGTH OF THE TUPLE IS :  7
THE TOTAL NUMBER OF TIMES GIVEN VALUE IS IN THE TUPLE :  1
THE INDEX OF GIVEN VALUE IS IN THE TUPLE talent :  5
yes present
1
2
3
4
5
talent
accurate
(1, 2, 3, 4, 5)
'''
