import random
import matplotlib.pyplot as plt
import sqlite3
con=sqlite3.connect('test.db')
c=con.execute("select * from student")
print("records inserted are :")
#con.execute("Create table guesses(user text not null,student text not null,department text not null,choice integer not null);")
dict1={}
for i in c:
    dict1[i[0]]=i[1]
#dict1 = {'ragul':'cse','arun':'mech','prathap':'it','vicky':'ece','somesh':'eee','manik':'civil','shyam':'mecht','anbu':'arch'}
#print(dict1)
key = list(dict1.keys())
temp = dict1.values()
val = list(temp)
stud=""
choice1=[]
choice2=[]
choice3=[]
choice4=[]
choice5=[]
choice6=[]
choice7=[]
choice8=[]
def pick():
    global stud
    stud = random.choice(key)
    print("Guess your friend " + stud + "'s department:")
def guess():
    guess1 = input()
    return guess1
total=1
while total<4:
    count = 1
    pick()
    while count < 9:
        guess2 = guess()
        if guess2.lower() == dict1[stud]:
            print("Great guess dude!")
            print("You have used " + str(count) + " chances")
            break
        else:
            print("Try again dude!")
            count = count + 1
    print("you have done it!")
    if count == 1:
        choice1.append(["usr"+str(total),stud,dict1[stud]])
        con.execute("Insert into guesses(user,student,department,choice) values(?,?,? ,?)",("usr"+str(total), stud, dict1[stud], count))
        con.commit()
        total = total + 1
    elif count == 2:
        choice2.append(["usr"+str(total),stud,dict1[stud]])
        con.execute("Insert into guesses(user,student,department,choice) values(?,?,? ,?)",("usr" + str(total), stud, dict1[stud], count))
        con.commit()
        total = total + 1
    elif count == 3:
        choice3.append(["usr"+str(total),stud,dict1[stud]])
        con.execute("Insert into guesses(user,student,department,choice) values(?,?,? ,?)",("usr" + str(total), stud, dict1[stud], count))
        con.commit()
        total = total + 1
    elif count == 4:
        choice4.append(["usr"+str(total),stud,dict1[stud]])
        con.execute("Insert into guesses(user,student,department,choice) values(?,?,? ,?)",("usr" + str(total), stud, dict1[stud], count))
        con.commit()
        total = total + 1
    elif count == 5:
        choice5.append(["usr"+str(total),stud,dict1[stud]])
        con.execute("Insert into guesses(user,student,department,choice) values(?,?,? ,?)",("usr" + str(total), stud, dict1[stud], count))
        con.commit()
        total = total + 1
    elif count == 6:
        choice6.append(["usr"+str(total),stud,dict1[stud]])
        con.execute("Insert into guesses(user,student,department,choice) values(?,?,? ,?)",("usr" + str(total), stud, dict1[stud], count))
        con.commit()
        total = total + 1
    elif count == 7:
        choice7.append(["usr"+str(total),stud,dict1[stud]])
        con.execute("Insert into guesses(user,student,department,choice) values(?,?,? ,?)",("usr" + str(total), stud, dict1[stud], count))
        con.commit()
        total = total + 1
    elif count == 8:
        choice8.append(["usr"+str(total),stud,dict1[stud]])
        con.execute("Insert into guesses(user,student,department,choice) values(?,?,? ,?)",("usr" + str(total), stud, dict1[stud], count))
        con.commit()
        total = total + 1


print("users guessed in single attempt",choice1)
print("users guessed in two attempt",choice2)
print("users guessed in three attempt",choice3)
print("users guessed in four attempt",choice4)
print("users guessed in five attempt",choice5)
print("users guessed in six attempt",choice6)
print("users guessed in seven attempt",choice7)
print("users guessed in eight attempt",choice8)

#Fetching data from the table
a1=con.execute("Select user,choice from guesses")
b1=a1.fetchall()
c1={key:val for key,val in b1}
"""
#Barchart
plt.bar(range(len(c1)), list(c1.values()), align='center')
plt.xticks(range(len(c1)), list(c1.keys()))
plt.show()
"""
con.close()
#print(list(c1.keys()))
#print(list(c1.values()))
#Pie chart
labels = list(c1.keys())
sizes = list(c1.values())
colors = ['gold', 'yellowgreen', 'orange']
explode = (0.05,0.05,0.05)
plt.pie(sizes, explode=explode,labels=labels,colors=colors, shadow=True, startangle=140)
plt.axis('equal')
plt.show()

