#dicttionaries
'''Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element
    Dictionary holds key:value pair. 
    Key value is provided in the dictionary to make it more optimized
    Dictionary must be unique and of immutable data type '''
#creation of empty dictionary
d={}
#creating a dictionary
d1={"talent":"acurate","ragul":"k7","boat":"rockerz",1:(1,2,3),2:"two"}

#accessing element using [] braces and key values
print d1["talent"]

#accessing element using d.get()
print(d1.get("boat"))

#adding elements to dictionary d1[new_key]=coressponding value
print d1
d1["newkey"]="winner"
print "new updated dict : ",d1
d1["dic"]={1:1,2:2}
print "new updated dict : ",d1

#del a element in dict

#del using del()
del d1["ragul"]
print "new updated dict : ",d1

#del using pop()
d1.pop(1)
print "new updated dict : ",d1

#deleting first element using popitem()
d1.popitem()
print "new updated dict : ",d1

#deleting a nested dict
del d1["dic"][1]
print "new updated dict : ",d1

#creating a copy of dict using d.copy()
d2=d1.copy()
print "copy of d1 : ",d2

#get all the list of values
print "list of values in dictionary : ",d1.values()

#get all the list of keys
print "list of keys in dictionary : ",d1.keys()

#whether given key is in dict ? using has_dict()
print "is key 2 in dictionary : ",d1.has_key(2)
print "is key talentin dictionary : ",d1.has_key("talent")

#print list of all (key,value) tuples
print "list of (key:value) in dictionary : ",d1.items()

#empty the dictionary using clear()
d1.clear()
print d1

#delete entire dict
del d1

'''
OUTPUT:
acurate
rockerz
{'ragul': 'k7', 1: (1, 2, 3), 2: 'two', 'talent': 'acurate', 'boat': 'rockerz'}
new updated dict :  {1: (1, 2, 3), 2: 'two', 'talent': 'acurate', 'newkey': 'winner', 'ragul': 'k7', 'boat': 'rockerz'}
new updated dict :  {1: (1, 2, 3), 2: 'two', 'talent': 'acurate', 'newkey': 'winner', 'dic': {1: 1, 2: 2}, 'ragul': 'k7', 'boat': 'rockerz'}
new updated dict :  {1: (1, 2, 3), 2: 'two', 'talent': 'acurate', 'newkey': 'winner', 'dic': {1: 1, 2: 2}, 'boat': 'rockerz'}
new updated dict :  {2: 'two', 'talent': 'acurate', 'newkey': 'winner', 'dic': {1: 1, 2: 2}, 'boat': 'rockerz'}
new updated dict :  {'talent': 'acurate', 'newkey': 'winner', 'dic': {1: 1, 2: 2}, 'boat': 'rockerz'}
new updated dict :  {'talent': 'acurate', 'newkey': 'winner', 'dic': {2: 2}, 'boat': 'rockerz'}
copy of d1 :  {'newkey': 'winner', 'talent': 'acurate', 'boat': 'rockerz', 'dic': {2: 2}}
list of values in dictionary :  ['acurate', 'winner', {2: 2}, 'rockerz']
list of keys in dictionary :  ['talent', 'newkey', 'dic', 'boat']
is key 2 in dictionary :  False
is key talentin dictionary :  True
list of (key:value) in dictionary :  [('talent', 'acurate'), ('newkey', 'winner'), ('dic', {2: 2}), ('boat', 'rockerz')]
{}'''
