# coding: utf-8

"""
Одиночка (Singleton) - паттерн, порождающий объекты.
Гарантирует, что у класса есть только один экземпляр, и предоставляет к нему глобальную точку доступа.
С помощью паттерна одиночка могут быть реализованы многие паттерны (абстрактная фабрика, строитель, прототип).
"""


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


obj1 = Singleton('MyInstance 1')
print(obj1.get_name())  # MyInstance 1

obj2 = Singleton('MyInstance 2')
print(obj2.get_name())  # MyInstance 1

if id(obj1) == id(obj2):
    print("Синглтон работает, обе переменные содержат один и тот же экземпляр")
else:
    print("Сбой синглтона, переменные содержат разные экземпляры ")