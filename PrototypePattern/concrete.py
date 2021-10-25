from copy import deepcopy

from PrototypePattern.prototype_1 import Prototype


class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)

