li = [5, 7, -22, 97, -54, -62, -77, 23, 73, 61] 
positive_list = list(filter(lambda x: x>0 , li))
negative_list = list(filter(lambda x: x<0,li))
print positive_list
print negative_list

'''
OUTPUT:
[5, 7, 97, 23, 73, 61]
[-22, -54, -62, -77]
'''
