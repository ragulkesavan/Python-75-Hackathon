'''->A local variable is a variable that is given local scope. 
   ->Local variable     
     references in the function or block in which it is declared override the same
     variable name in the larger scope
   ->The local variables can be used only within its function or block
   ->The cannot be accessed outside the block it is defined'''

string_global="I am global variable"
# string_glogal is in global scope and hence can be referenced any where

def func():
    string_local="I am a local variable"# string_local is inside the function func() thus accessible only inside func() and not outside the func() function
    
    print "string_global inside func():",string_global #accessing global variable inside the func()
    print "string_local inside func(): ",string_local#accessing local variable inside the func()
func()
'''trying to execute the print function outside produces error as the variable cannot be accessed'''

print "string_global in global scope:",string_global#accessing global variable 
'''
OUTPUT:
string_global inside func(): I am global variable
string_local inside func():  I am a local variable
string_global in global scope: I am global variable
'''
