#RAGNE FUNCTION USING 3 ARGUMENTS
'''the def of range function is range([start,stop,step])
PARAMETER	DESCRIPTION
start	(optional) Starting point of the sequence. It defaults to 0.
stop	(required) Endpoint of the sequence. This item will not be included in the      sequence.
step	(optional) Step size of the sequence. It defaults to 1.
         
The range function returns a list.The list strats with start value passed as arguement,the next elements got by incrementing start value by step value,the list must end with a value < than stop value'''

n=int(input("ENTER THE N VALUE : "))
l1=range(0,n,1)
print "WHEN STEP=1 LIST = ",l1
'''THE range() FUNCTION ABOVE RETURNS A LIST STARTING WITH 0 THEN THE FOLLOWING VALUES ARE GOT BY ADDING +1.THUS THE LIST GOES AS 0,1,2,3,4,5,6,..... THE END MUST BE LESS THAN STOP=N=8, SO THE LIST IS 0,1,2,3,4,5,6,7 '''
l2=range(0,n,2)
print "WHEN STEP=2 LIST = ",l2
'''THE range() FUNCTION ABOVE RETURNS A LIST STARTING WITH 0 THEN THE FOLLOWING VALUES ARE GOT BY ADDING +2.THUS THE LIST GOES AS 0,2,4,6,..... THE END MUST BE LESS THAN STOP=N=8, SO THE LIST IS 0,2,4,6 '''
l3=range(0,n,3)
print "WHEN STEP=3 LIST = ",l3
'''THE range() FUNCTION ABOVE RETURNS A LIST STARTING WITH 0 THEN THE FOLLOWING VALUES ARE GOT BY ADDING +1.THUS THE LIST GOES AS 0,3,6,..... THE END MUST BE LESS THAN STOP=N=8, SO THE LIST IS 0,3,6'''
