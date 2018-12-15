phone=set(["mi","apple","samsung","giomee","jio","nokia","karbon"])
tv=set(["samsung","apple","onida","vediocon"])
brand=phone.difference(tv)
print "brands in phone : ",phone
print "brands in tv : ",tv
print "phone brands that do not have tv : ",brand

'''
OUTPUT:
brands in phone :  set(['apple', 'samsung', 'jio', 'nokia', 'mi', 'giomee', 'karbon'])
brands in tv :  set(['onida', 'vediocon', 'apple', 'samsung'])
phone brands that do not have tv :  set(['giomee', 'jio', 'nokia', 'mi', 'karbon'])
'''
