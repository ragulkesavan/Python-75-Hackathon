import pdb
pdb.set_trace()

def  total(a):
  sum=0
  for i in range(1,b+1): # using unknown var b
    sum=sum+sqre(i)
  print("total squares  is",sum)
def sqre(b):
  return b*b
total(8)


'''
OTPUT STEP BY STEP
ragul@ragul-HP-Pavilion-Notebook:~/Downloads$ python3 debug.py
> /home/ragul/Downloads/debug.py(4)<module>()
-> def  total(a):
(Pdb) step
> /home/ragul/Downloads/debug.py(9)<module>()
-> def sqre(b):
(Pdb) step
> /home/ragul/Downloads/debug.py(11)<module>()
-> total(8)
(Pdb) step
--Call--
> /home/ragul/Downloads/debug.py(4)total()
-> def  total(a):
(Pdb) step
> /home/ragul/Downloads/debug.py(5)total()
-> sum=0
(Pdb) step
> /home/ragul/Downloads/debug.py(6)total()
-> for i in range(1,b+1):
(Pdb) step
NameError: name 'b' is not defined ---> error is detected here
> /home/ragul/Downloads/debug.py(6)total()
-> for i in range(1,b+1):
(Pdb)


'''
