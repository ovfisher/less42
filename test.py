class Test():
    def __init__(self):
        self.public = 'public'
        self._protected = 'protected'
        self.__private = 'private'
    def get_private(self):
        return self.__private
    def set_private(self,value):
        self.__private = value

class Test2:
    def public_func(self):
        print('public')
    def _protected_func(self):
        print('_protectec')
    def __private_func(self):
        print('__private')
    def test_private(self):
        self.__private_func()

t = Test2()
t.public_func()
t._protected_func()
t.test_private()

test = Test()
print(test.public)
print(test._protected)
test.set_private('test')
print(test.get_private())