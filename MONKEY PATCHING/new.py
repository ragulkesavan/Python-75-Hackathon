import mod
print("address of func() function in mod module",id(mod.func))

def newfunc():
    print("I'm newfunc() going to monkey patch func() function")
mod.func=newfunc
print("address of func() function after patching is ",id(mod.func))
