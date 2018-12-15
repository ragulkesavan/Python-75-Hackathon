#FOR LOOP

'''
FOR LOOPS ARE USED FOR SEQUENTIAL TRAVERSEL
FOR EXAMPLE GIVEN A LIST WE CAN TRAVERSE SEQUENTIALLY STARTING FROM THE FIRST ELEMENT
'''
#USING RANGE FUNCTION
for i in range(0,20):
  print i
#ACCESSING USING INDEX
l=[1,4,2,3,5]
max=0
for i in range(len(l)):
  if max<l[i]:
    max=l[i]
print "maximum : ",max
#SEQUENTIAL TRAVERSEL USING LIST
for i in [1,6,4,3,2,6,8,2]:
  print i

#COUNTING LENGTH
count=0
for i in "string":
  count=count+1
print "string lenght is : ",count

#SEQUENTIALY  ACCESSING THE DICT AND APPENDING IT IN LIST 
l=[]
for i in {1:2,2:3,3:4}:
  l.append(i)
print l


'''
OUTPUT:
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
maximum :  5
1
6
4
3
2
6
8
2
string lenght is :  6
[1, 2, 3]
'''
