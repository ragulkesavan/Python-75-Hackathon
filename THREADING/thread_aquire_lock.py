from thread import start_new_thread, allocate_lock


lock = allocate_lock()
def chess(a):
    """Calculates the total possible square of a*a chess board"""
    sum=0
    copy=a
    while a>0:
        sum=sum+a*a
        a=a-1
    lock.acquire()
    print "\nthe total possible squares in a*a chess board of a=",copy," : ",sum
    lock.release()

start_new_thread(chess,(99,))
start_new_thread(chess,(999,))
start_new_thread(chess,(1733,))

c = raw_input("Type something to quit.")

'''
OUTPUT:
Type something to quit.
the total possible squares in a*a chess board of a= 99  :  328350

the total possible squares in a*a chess board of a= 999  :  332833500

the total possible squares in a*a chess board of a= 1733  :  1736401879
a

'''
