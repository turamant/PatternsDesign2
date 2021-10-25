from copy import deepcopy

from PrototypePattern.prototype_1 import Prototype


class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = "Knight"
        file_name = "{}_{}.dat".format(self.unit_type, level)
        with open(file_name, "r") as parametr_file:
            lines = parametr_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return f"Type: {self.unit_type}," \
               f"Life: {self.life}, " \
               f"Speed: {self.speed}, " \
               f"Attack Power: {self.attack_power}, " \
               f"Attack Range: {self.attack_range}, " \
               f"Weapon: {self.weapon}"
    def clone(self):
        return deepcopy(self)

class Archer(Prototype):
    def __init__(self, level):
        self.unit_type = "Archer"
        file_name = "{}_{}.dat".format(self.unit_type, level)
        with open(file_name, "r") as parametr_file:
            lines = parametr_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return f"Type: {self.unit_type}, " \
               f"Life: {self.life}, " \
               f"Speed: {self.speed}, " \
               f"Attack Power: {self.attack_power}, " \
               f"Attack Range: {self.attack_range}, " \
               f"Weapon: {self.weapon}"

    def clone(self):
        return deepcopy(self)

class Barracks:
    def __init__(self):
        self.units = {
            "knight": {
                1: Knight(1),
                2: Knight(2)
            },
            "archer": {
                1: Archer(1),
                2: Archer(2)
            }


        }
    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()



if __name__ == '__main__':
    barracks = Barracks()
    knight1 = barracks.build_unit("knight", 1)
    archer1 = barracks.build_unit("archer", 1)
    print("[knight1] - {}".format(knight1))
    print("[archer1] - {}".format(archer1))
