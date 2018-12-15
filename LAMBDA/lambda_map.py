li = [5, 7, -22, 97, -54, -62, -77, 23, 73, 61] 
positive_list = list(map(lambda x: x>0 , li))
negative_list = list(map(lambda x: x<0,li))
print positive_list
print negative_list

'''
OUTPUT:
[True, True, False, True, False, False, False, True, True, True]
[False, False, True, False, True, True, True, False, False, False]
'''
