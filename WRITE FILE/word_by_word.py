#WRITING INTO FILE LINE BY LINE
#opening file in w mode

f=open("lyrics.txt","w")

''' USING write() FUNCTION WE CAN WRITE WORD BY WORD INTO FILES ,EACH ATTRIBUTE OF write() IS A WORD STRING'''

f.write("Spent ")
f.write("24 ")
f.write("hours\n")#AS IT ENDS THE LINE "\n" IS USED
f.write("I ")
f.write("need ")
f.write("more ")
f.write("hours ")
f.write("with ")
f.write("you\n") #AS IT ENDS THE LINE "\n" IS USED
f.write("You ")
f.write("spend ")
f.write("the ")
f.write("week") 
f.write("end\n")#AS IT ENDS THE LINE "\n" IS USED
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
