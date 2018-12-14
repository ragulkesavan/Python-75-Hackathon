'''PROBLEM: Calculate the total number of possible squares in a chess board of n*n size (n is got from user)'''
def chess(n):
    if n==1:
        return 1
    else :
        return (n*n)+chess(n-1)
n=int(input("give the n-chess board size : "))
print("\nthe chess board has "+str(chess(n))+" possible squares")

'''
OUTPUT:
  give the n-chess board size : 8
  the chess board has 204 possible squares
'''
