import threading
def chess(self,a):
   sum=0
   copy=a
   while a>0:
       sum=sum+a*a
       a=a-1
   print "\nthe total possible squares in a*a chess board of a=",copy," : ",sum
  
t1 = threading.Thread(target=chess,args=(99,))
t1.start()
t1.join()
