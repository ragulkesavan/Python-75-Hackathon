import pdb
pdb.set_trace()

def  total(a):
  sum=0
  for i in range(1,a+1):
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
> /home/ragul/Downloads/debug.py(12)<module>()
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
-> for i in range(1,a+1):
(Pdb) step
> /home/ragul/Downloads/debug.py(7)total()
-> sum=sum+sqre(i)
(Pdb) step
--Call--
> /home/ragul/Downloads/debug.py(9)sqre()
-> def sqre(b):
(Pdb) step
> /home/ragul/Downloads/debug.py(11)sqre()
-> return b*b
(Pdb) step
--Return--
> /home/ragul/Downloads/debug.py(11)sqre()->1
-> return b*b
(Pdb) step
> /home/ragul/Downloads/debug.py(6)total()
-> for i in range(1,a+1):
(Pdb) step
> /home/ragul/Downloads/debug.py(7)total()
-> sum=sum+sqre(i)
(Pdb) step
--Call--
> /home/ragul/Downloads/debug.py(9)sqre()
-> def sqre(b):
(Pdb) step
> /home/ragul/Downloads/debug.py(11)sqre()
-> return b*b
(Pdb) step
--Return--
> /home/ragul/Downloads/debug.py(11)sqre()->4
-> return b*b
(Pdb) step
> /home/ragul/Downloads/debug.py(6)total()
-> for i in range(1,a+1):
(Pdb) step
> /home/ragul/Downloads/debug.py(7)total()
-> sum=sum+sqre(i)
(Pdb) step
--Call--
> /home/ragul/Downloads/debug.py(9)sqre()
-> def sqre(b):
(Pdb) step
> /home/ragul/Downloads/debug.py(11)sqre()
-> return b*b
(Pdb) step
--Return--
> /home/ragul/Downloads/debug.py(11)sqre()->9
-> return b*b
(Pdb) step
> /home/ragul/Downloads/debug.py(6)total()
-> for i in range(1,a+1):
(Pdb) step
> /home/ragul/Downloads/debug.py(7)total()
-> sum=sum+sqre(i)
(Pdb) step
--Call--
> /home/ragul/Downloads/debug.py(9)sqre()
-> def sqre(b):
(Pdb) step
> /home/ragul/Downloads/debug.py(11)sqre()
-> return b*b
(Pdb) step
--Return--
> /home/ragul/Downloads/debug.py(11)sqre()->16
-> return b*b
(Pdb) step
> /home/ragul/Downloads/debug.py(6)total()
-> for i in range(1,a+1):
(Pdb) step
> /home/ragul/Downloads/debug.py(7)total()
-> sum=sum+sqre(i)
(Pdb) step
--Call--
> /home/ragul/Downloads/debug.py(9)sqre()
-> def sqre(b):
(Pdb) step
> /home/ragul/Downloads/debug.py(11)sqre()
-> return b*b
(Pdb) step
--Return--
> /home/ragul/Downloads/debug.py(11)sqre()->25
-> return b*b
(Pdb) step
> /home/ragul/Downloads/debug.py(6)total()
-> for i in range(1,a+1):
(Pdb) step
> /home/ragul/Downloads/debug.py(7)total()
-> sum=sum+sqre(i)
(Pdb) step
--Call--
> /home/ragul/Downloads/debug.py(9)sqre()
-> def sqre(b):
(Pdb) step
> /home/ragul/Downloads/debug.py(11)sqre()
-> return b*b
(Pdb) step
--Return--
> /home/ragul/Downloads/debug.py(11)sqre()->36
-> return b*b
(Pdb) step
> /home/ragul/Downloads/debug.py(6)total()
-> for i in range(1,a+1):
(Pdb) step
> /home/ragul/Downloads/debug.py(7)total()
-> sum=sum+sqre(i)
(Pdb) step
--Call--
> /home/ragul/Downloads/debug.py(9)sqre()
-> def sqre(b):
(Pdb) step
> /home/ragul/Downloads/debug.py(11)sqre()
-> return b*b
(Pdb) step
--Return--
> /home/ragul/Downloads/debug.py(11)sqre()->49
-> return b*b
(Pdb) step
> /home/ragul/Downloads/debug.py(6)total()
-> for i in range(1,a+1):
(Pdb) step
> /home/ragul/Downloads/debug.py(7)total()
-> sum=sum+sqre(i)
(Pdb) step
--Call--
> /home/ragul/Downloads/debug.py(9)sqre()
-> def sqre(b):
(Pdb) step
> /home/ragul/Downloads/debug.py(11)sqre()
-> return b*b
(Pdb) step
--Return--
> /home/ragul/Downloads/debug.py(11)sqre()->64
-> return b*b
(Pdb) step
> /home/ragul/Downloads/debug.py(6)total()
-> for i in range(1,a+1):
(Pdb) next
> /home/ragul/Downloads/debug.py(8)total()
-> print("total squares  is",sum)
(Pdb) step
total squares  is 204
--Return--
> /home/ragul/Downloads/debug.py(8)total()->None
-> print("total squares  is",sum)
(Pdb) step
--Return--
> /home/ragul/Downloads/debug.py(12)<module>()->None
-> total(8)
(Pdb) step
--Call--

'''
