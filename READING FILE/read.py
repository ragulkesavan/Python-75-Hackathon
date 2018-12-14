f=open("girlslikeyou.txt","r")
#read() function returns all the content in the file as a single string
f.read()
#returns all values in girlslikeyou.txt

f.seek(0)
#seek moves read pointer to starting of file

f.read(10)
#this will read first 10 letters or char in file

'''
OUTPUT:
"Spent 24 hours\nI need more hours with you\nYou spent the weekend\nGetting even, ooh ooh\nWe spent the late nights\nMaking things right, between us\nBut now it's all good baby\nRoll that Backwood baby\nAnd play me close\n'Cause girls like you\nRun around with guys like me\n'Til sundown, when I come through\nI need a girl like you, yeah yeah\nGirls like you\nLove fun, yeah me too\nWhat I want when I come through\nI need a girl like you, yeah yeah\nYeah yeah yeah\nYeah yeah yeah\nI need a girl like you, yeah yeah\nYeah yeah yeah\nYeah yeah yeah\nI need a girl like you, yeah yeah\nI spent last night\nOn the last flight to you\nTook a whole day up\nTrying to get way up, ooh ooh\nWe spent the daylight\nTrying to make things right between us\nAnd now it's all good baby\nRoll that Backwood baby\nAnd play\xe2\x80\xa6\n"
'Spent 24 h'
'''
