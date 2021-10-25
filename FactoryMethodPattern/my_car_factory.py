

class Car:
    def __init__(self, color, year):
        self.color = color
        self.year = year

    def information(self):
        print(self.color, self.year)


    @staticmethod
    def factory(type):
        if type == "Bmv":
            return Bmv("blue", 1995)
        if type == "Mersedes":
            return Mersedes("red", 2002)
        assert 0, "Bad car request: " + type

class Bmv(Car):
    def __str__(self):
        return f"{__class__.__name__}: {self.year}"

class Mersedes(Car):
    def __str__(self):
        return f"{__class__.__name__}: {self.year}"



if __name__ == '__main__':
    newcar = Car.factory("Mersedes")
    newcar.information()
    print(newcar)



