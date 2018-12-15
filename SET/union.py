phone=set(["mi","apple","samsung","giomee","jio","nokia","karbon"])
tv=set(["samsung","apple","onida","vediocon"])
brand=phone.union(tv)
print "brands in phone : ",phone
print "brands in tv : ",tv
print "union of brands : ",brand

'''
OUTPUT:
brands in phone :  set(['apple', 'samsung', 'jio', 'nokia', 'mi', 'giomee', 'karbon'])
brands in tv :  set(['onida', 'vediocon', 'apple', 'samsung'])
union of brands :  set(['vediocon', 'apple', 'samsung', 'onida', 'jio', 'nokia', 'mi', 'giomee', 'karbon'])
'''
