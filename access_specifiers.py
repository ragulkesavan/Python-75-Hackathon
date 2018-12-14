class parent:
    def __init__(self,a,b,c):
        self.a=a
        self._b=b
        self.__c=c
    def val(self):
        print self.__c
c=parent(1,2,3)
print c.a
print c._b
print c.val()
