#WRITING INTO FILE LINE BY LINE
#opening file in w mode
f=open("lyrics.txt","w")
''' USING write() FUNCTION WE CAN WRITE LINE BY LINE INTO FILES ,EACH ATTRIBUTE OF write() IS A LINE STRING AND SHOULD END WITH "\n" OR EOL '''
f.write("Spent 24 hours\n")
f.write("I need more hours with you\n")
f.write("You spend the week end\n")
f.close()
f=open("lyrics.txt","r")
print f.read()
f.close()
'''
OUTPUT
Spent 24 hours
I need more hours with you
You spend the week end
'''
