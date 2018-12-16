import matplotlib.pyplot as plt
import sqlite3
con=sqlite3.connect('test.db')
c=con.execute("select * from students")
print("records inserted are :")
#Run this file after running g.py

#Fetching data from the table
a1=con.execute("Select user,choice from guesses")
b1=a1.fetchall()
c1={key:val for key,val in b1}
#Barchart
plt.bar(range(len(c1)), list(c1.values()), align='center')
plt.xticks(range(len(c1)), list(c1.keys()))
plt.show()
