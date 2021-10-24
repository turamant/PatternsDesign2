class OnlyOne(object):
    class __OnlyOne:
        def __init__(self):
            self.val = None
        def __str__(self):
            return "{0!r} {1}".format(
              self, self.val
            )
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne()
        return OnlyOne.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)


if __name__=='__main__':
    obj1 = OnlyOne()
    obj1.val = 'Object value 1'
    print(" print object1:", obj1)
    print("---------")
    obj2 = OnlyOne()
    obj2.val = 'Object value 2'
    print(" print object2:", obj2)
    print("---------")
    obj3 = OnlyOne()
    obj3.val = 'Object value 3'
    print(" print object3:", obj3)
    print("---------")

