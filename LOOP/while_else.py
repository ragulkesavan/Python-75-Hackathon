#WHILE LOOP WITH ELSE

l=["talent","accurate","torento","canada","all","is","well"]
print l
print "YOU ARE GIVEN 3 CHANCE TO GIVE A STRING AND TO CHECK WHETHER IT IS IN LIST"
i=0
str=input()
while (str in l) and i<3:
  print "yes"
  i=i+1
  str=input()
else :
  print "no either not in list or chance has ended"

'''
OUTPUT:
['talent', 'accurate', 'torento', 'canada', 'all', 'is', 'well']
YOU ARE GIVEN 3 CHANCE TO GIVE A STRING AND TO CHECK WHETHER IT IS IN LIST
"talent"
yes
"accurate"
yes
"all"
yes
"all" 
no either not in list or chance has ended
'''
