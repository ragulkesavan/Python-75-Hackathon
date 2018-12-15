phone=set(["mi","apple","samsung","giomee","jio","nokia","karbon"])
tv=set(["samsung","apple","onida","vediocon"])
s=set([1,2,3,4,5])
t=set([1,3,5])

brand=phone|tv
print "brands in phone : ",phone
print "brands in tv : ",tv
print "union of brands : ",brand


brand=phone&tv
print "brands in phone : ",phone
print "brands in tv : ",tv
print "common brands : ",brand


brand=phone-tv
print "brands in phone : ",phone
print "brands in tv : ",tv
print "phone brands that do not have tv : ",brand


if "onida" in tv:
    print "onida is tv brand"
elif "onida" not in phone:
    print "onida is not a mobile brand "# containment check



if phone==tv:
    print "sets are equivalent"# s1 is equivalent to s2
else :
    print "sets are not equivalent"
    
if phone!=tv:
    print "sets are not equivalent"# s1 is equivalent to s2
else :
    print "sets are equivalent"
    

if s<t:
    print s," is a subset of ",t
elif s>t:
    print t," is a subset of ",s


'''
OUTPUT:

brands in phone :  set(['apple', 'samsung', 'jio', 'nokia', 'mi', 'giomee', 'karbon'])
brands in tv :  set(['onida', 'vediocon', 'apple', 'samsung'])
union of brands :  set(['vediocon', 'apple', 'samsung', 'onida', 'jio', 'nokia', 'mi', 'giomee', 'karbon'])
brands in phone :  set(['apple', 'samsung', 'jio', 'nokia', 'mi', 'giomee', 'karbon'])
brands in tv :  set(['onida', 'vediocon', 'apple', 'samsung'])
common brands :  set(['apple', 'samsung'])
brands in phone :  set(['apple', 'samsung', 'jio', 'nokia', 'mi', 'giomee', 'karbon'])
brands in tv :  set(['onida', 'vediocon', 'apple', 'samsung'])
phone brands that do not have tv :  set(['giomee', 'jio', 'nokia', 'mi', 'karbon'])
onida is tv brand
sets are not equivalent
sets are not equivalent
set([1, 3, 5])  is a subset of  set([1, 2, 3, 4, 5])
'''
