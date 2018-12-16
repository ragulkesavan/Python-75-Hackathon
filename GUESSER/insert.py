import sqlite3
con=sqlite3.connect('test.db')
print("Opened db successfully!")
con.execute("Create table students(name text not null,department text not null);")
print("Table created!")
con.execute("Insert into students(name,department) values('ragul','cse');")
con.execute("Insert into students(name,department) values('arun','mech');")
con.execute("Insert into students(name,department) values('prathap','it');")
con.execute("Insert into students(name,department) values('vicky','ece');")
con.execute("Insert into students(name,department) values('somesh','eee');")
con.execute("Insert into students(name,department) values('manik','civil');")
con.execute("Insert into students(name,department) values('shyam','mecht');")
con.execute("Insert into students(name,department) values('anbu','arch');")
con.commit()
print("Records done!!")
c=con.execute("select * from students")
print("records inserted are :")
for i in c:
    print(i)
'''name_list=con.execute("select name from students")
name_list=list(name_list)
print(name_list)

dept_list=con.execute("select department from students")
dept_list=list(dept_list)
print(dept_list)

c=con.execute("select * from students")
x=c.fetchall()
dict1={key:val for key,val in x}

#print(dict1)'''

con.close()

