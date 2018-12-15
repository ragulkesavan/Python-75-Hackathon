from thread import start_new_thread

def chess(a):
    """Calculates the total possible square of a*a chess board"""
    copy=a
    sum=0
    while a>0:
        sum=sum+a*a
        a=a-1
    print "\nthe total possible squares in a*a chess board of a=",copy," : ",sum


start_new_thread(chess,(99,))
start_new_thread(chess,(999,))
start_new_thread(chess,(1733,))

c = raw_input("Type something to quit.")

'''
OUTPUT:
ragul@ragul-HP-Pavilion-Notebook:~/py4e$ python thread.py
Type something to quit.
the total possible squares in a*a chess board of a= 99  :  328350

the total possible squares in a*a chess board of a= 999  :  332833500

the total possible squares in a*a chess board of a= 1733  :  1736401879
a
ragul@ragul-HP-Pavilion-Notebook:~/py4e$ python thread.py
Type something to quit.
the total possible squares in a*a chess board of a= 99  :  328350

the total possible squares in a*a chess board of a= 999  :  332833500

the total possible squares in a*a chess board of a= 1733  :  1736401879
a
ragul@ragul-HP-Pavilion-Notebook:~/py4e$ python thread.py
Type something to quit.
the total possible squares in a*a chess board of a= 99  :  328350

the total possible squares in a*a chess board of a= 1733  :  1736401879
the total possible squares in a*a chess board of a=
 999  :  332833500
a
ragul@ragul-HP-Pavilion-Notebook:~/py4e$ python thread.py
Type something to quit.
the total possible squares in a*a chess board of a= 99  :  328350

the total possible squares in a*a chess board of a=
the total possible squares in a*a chess board of a= 1733 999   :  1736401879 : 
 332833500
a    
ragul@ragul-HP-Pavilion-Notebook:~/py4e$ python thread.py
Type something to quit.
the total possible squares in a*a chess board of a= 99  :  328350

the total possible squares in a*a chess board of a= 999  :  332833500

the total possible squares in a*a chess board of a= 1733  :  1736401879
a
ragul@ragul-HP-Pavilion-Notebook:~/py4e$ python thread.py
Type something to quit.
the total possible squares in a*a chess board of a= 99  :  328350

the total possible squares in a*a chess board of a= 999  :  332833500

the total possible squares in a*a chess board of a= 1733  :  1736401879
a
ragul@ragul-HP-Pavilion-Notebook:~/py4e$ python thread.py
Type something to quit.
the total possible squares in a*a chess board of a= 99  :  328350

the total possible squares in a*a chess board of a= 1733  :  1736401879
 
the total possible squares in a*a chess board of a= 999  :  332833500
a
ragul@ragul-HP-Pavilion-Notebook:~/py4e$ python thread.py
Type something to quit.
the total possible squares in a*a chess board of a= 99  :  328350

the total possible squares in a*a chess board of a= 1733  :  1736401879

the total possible squares in a*a chess board of a= 999  :  332833500
a
ragul@ragul-HP-Pavilion-Notebook:~/py4e$ python thread.py
Type something to quit.
the total possible squares in a*a chess board of a= 99  : 
the total possible squares in a*a chess board of a= 328350 
999  :  332833500

the total possible squares in a*a chess board of a= 1733  :  1736401879
^CTraceback (most recent call last):
  File "thread.py", line 17, in <module>
    c = raw_input("Type something to quit.")
KeyboardInterrupt
ragul@ragul-HP-Pavilion-Notebook:~/py4e$ 

'''
