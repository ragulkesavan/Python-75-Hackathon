#STRING OPERATIONS
string="tallent accurate"
str1="MaDuRaI"
str2="I, am, CODER"
'''all string operations do not change individual elements in string but alters the existing string and returns a new string'''
#printing string
print(string)

#printing individual element in string-using [index]
print(string[2])

#SLICING STRING USING SLICING OPERATOR-slices [a:b] string from ath element to b-1th element and returns a new string
new=string[3:12]
print "new sliced string is ",new
#SLICING WITH 0VE VALUE
print "new string :",string[3:-2]
#SLICING WITH 3 VALUES-slices string as above but leaves all values between the step values
new2=string[0:12:2] 
print "new sliced string is ",new2

#length of string
print "length of string is",len(string)

#changing all the elements to lower case using lower(input_string)
#returns a new string of all elements lower case of input string
print "string is ",str1
print "using lower() new string is ",str1.lower()

#changing all the elements to upper case using upper(input_string)
#returns a new string of all upper lower case of input string
print "string is ",str1
print "using upper() new string is ",str1.upper()

#spliting a string using split()
#splits the input string and returs a list of elements based on the element of split
print str2.split(",")

#replace elements in string using replace("","")
#replaces all a to b and returns a new string
print "string is ",string
print "using replace() new string is ",string.replace("a","b")

#string concatenation using + operator
#joins two string and returns a new string
print "concatenated string :",str2+str1

#striping white spaces at beginning and end of string
a="  haii  "
print "string is :",a
print "after striping :",a.strip()

#string mul
print string*3#prints string 3

'''
OUTPUT:
tallent accurate
l
new sliced string is  lent accu
new string : lent accura
new sliced string is  tletac
length of string is 16
string is  MaDuRaI
using lower() new string is  madurai
string is  MaDuRaI
using upper() new string is  MADURAI
['I', ' am', ' CODER']
string is  tallent accurate
using replace() new string is  tbllent bccurbte
concatenated string : I, am, CODERMaDuRaI
string is :   haii  
after striping : haii
tallent accuratetallent accuratetallent accurate
'''
