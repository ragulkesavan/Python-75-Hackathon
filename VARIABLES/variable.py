#variables
'''python do not need to explicitly specify the data type of variable ,it automatically sets data type according to value '''
a=10#int
b=10.11#float
c=3.14j#complex
d='t'#string
e="talent acurate"#string

#printing the type of the variable
print type(a)
print type(b)
print type(c)
print type(d)
print type(e)

f,g=1,"torento"

print a,b,c
print str(a)+str(b)+e+str(c)

#int type variable after executing the following statement refers the string
a="int to string vavriable"

print a
#hence in python we need not worry about data type

'''
OUTPUT
<type 'int'>
<type 'float'>
<type 'complex'>
<type 'str'>
<type 'str'>
10 10.11 3.14j
1010.11talent acurate3.14j
int to string vavriable
'''
