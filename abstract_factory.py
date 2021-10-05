# coding: utf-8

"""
Абстрактная фабрика (Abstract factory, Kit) - паттерн, порождающий объекты.
Предоставляет интерфейс для создания семейств взаимосвязанных или взаимозависимых объектов,
не специфицируя их конкретных классов.
Классы абстрактной фабрики часто реализуются фабричными методами,
но могут быть реализованы и с помощью паттерна прототип.
"""


class AbstractFactory:
    def create_product1(self):
        raise NotImplementedError()

    def create_product2(self):
        raise NotImplementedError()


class AdminForm:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class UserForm:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class ConcreteFactory1(AbstractFactory):
    def create_product1(self):
        return AdminForm('форма регистрации администратора')

    def create_product2(self):
        return UserForm('форма регистрации юзера')


class ConcreteFactory2(AbstractFactory):
    def create_product1(self):
        return AdminForm('форма активации администратора')

    def create_product2(self):
        return UserForm('форма активации юзера')


def get_factory(ident):
    if ident == 0:
        return ConcreteFactory1()
    elif ident == 1:
        return ConcreteFactory2()

if __name__=='__main__':
    factory = get_factory(0)
    print(factory.create_product1())
    print(factory.create_product2())
