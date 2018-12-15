import random
d={"ragul":"cse","arun":"mech","prathap":"it","vicky":"ece","somesh":"eee","manik":"civil","shyam":"mecht","anbu":"arch"}
grand_total=1
total=1
choice1=[]
choice2=[]
choice3=[]
choice4=[]
choice5=[]
choice6=[]
choice7=[]
choice8=[]
while total<81:
  for i in d.keys():
    l=["cse","mech","it","eee","ece","civil","mecht","arch"]
    count=1
    while count<9:
      r=random.choice(l)
      if r==d[i]:
        grand_total=grand_total+1
        break
      else :
        l.remove(r)
        count=count+1
    if count==1 and len(choice1)<10:
      choice1.append(total)
      total=total+1
    elif count==2 and len(choice2)<10:
      choice2.append(total)
      total=total+1
    elif count==3 and len(choice3)<10:
      choice3.append(total)
      total=total+1
    elif count==4 and len(choice4)<10:
      choice4.append(total)
      total=total+1
    elif count==5 and len(choice5)<10:
      choice5.append(total)
      total=total+1
    elif count==6 and len(choice6)<10:
      choice6.append(total)
      total=total+1
    elif count==7 and len(choice7)<10:
      choice7.append(total)
      total=total+1
    elif count==8 and len(choice8)<10:
      choice8.append(total)
      total=total+1
    
print "dictionary is : ",d
print "departments : ",l
print "users guessed in single attempt",choice1
print "users guessed in two attempt",choice2
print "users guessed in three attempt",choice3
print "users guessed in four attempt",choice4
print "users guessed in five attempt",choice5
print "users guessed in six attempt",choice6
print "users guessed in seven attempt",choice7
print "users guessed in eight attempt",choice8
