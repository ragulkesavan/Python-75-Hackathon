#RANDOM NUMBR GENERATION USING METHODS IN random lib
import random
'''TO CREATE A RANDOM NUMBER FLOAT TYPE NUMBER TWO FUNCTIONS ARE USED
   1.uniform(a,b)
   2.random()'''

print "random number using random() function : ",random.random()

#random() function creates a float type random number of range between 0 to 1

print "random number using uniform() function : ",random.uniform(2.9,3)

#uniform(a,b) function creates a float type random number of range between a to b

'''TO SELECT A RANDOM NUMBER FROM A LIST WE USE choice(list), randrange(start,stop,step)'''
l=[1,2,3,4,5,6,7]

print "random number using choice() function : ",random.choice(l)

#choice(list) function gets list as input and selects a random number from it

print "random number using choice() function : ",random.randrange(5,50,5)

#randrange(start,stop,step) function gets list generated in the same way as range function do by using the arguements passed as input and selects a random number from the list created
'''USING seed() ALONG WITH random() seed(a) function seeds a random number to a paticular seed number 'a' '''
random.seed(10)
print "random number using seed() function for 10: ",random.random()

random.seed(11)
print "random number using seed() function for 11: ",random.random()

random.seed(10)
print "random number using seed() function for 10: ",random.random()," same value appear for seeked value 10"

'''SAMPLE OUTPUT:
random number using random() function :  0.952847382851
random number using uniform() function :  2.90502495936
random number using choice() function :  6
random number using choice() function :  10
random number using seed() function for 10:  0.57140259469
random number using seed() function for 11:  0.45237955351
random number using seed() function for 10:  0.57140259469  same value appear for seeked value 10'''
