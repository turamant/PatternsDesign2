import abc


class Car:
    def __init__(self):
        self.name = "Автомобильный завод"

    def detail(self):
        return self.name

class Airplan:
    def __init__(self):
        self.name = "Самолетный завод"

    def detail(self):
        return self.name

    def __str__(self):
        return f"Object:{__class__.__name__}: {self.name}"

class AbstractFactory:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def make_object(self):
        return

class CarFactory(AbstractFactory):
    def make_object(self):
        return Car()

class AirplanFactory(AbstractFactory):
    def make_object(self):
        return Airplan()





lst = []
dic = {}
air1 = AirplanFactory().make_object()
for i in range(10000):
    dic[i] = air1

for k, v in dic.items():
    print(k,":",v)
