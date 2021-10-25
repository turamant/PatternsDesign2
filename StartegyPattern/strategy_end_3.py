'''В традиционной реализации мы использовали типизацию утки.
Теперь мы будем использовать еще один мощный инструмент Python для написания
чистого кода — используя функции, как если бы они были любым другим значением.
Это означает, что мы можем передать функцию классу-исполнителю без предварительной
упаковки функции в собственный класс.
Это не только значительно сократит объем кода, который нам придется писать в долгосрочной
перспективе, но также облегчит чтение и тестирование нашего кода,
поскольку мы можем передавать аргументы функциям и утверждать, что они
возвращают ожидаемое значение.
class StrategyExecutor:
    def __init__(self, func=None):
        if func is not None:
            self.execute = func

    def execute(self, *args):
        print("Strategy not implemented..")

Поскольку мы уже передаем функции, мы могли бы также воспользоваться преимуществами
первоклассных функций и отказаться от объекта-исполнителя в нашей реализации,
оставив нам очень элегантное решение проблемы динамической стратегии.
'''

'''
На самом деле используем передачу функции и аргументов в функцию
'''
def executor(arg1, arg2, func=None):
    if func is None:
        return "Strategy not implemented.."
    return func(arg1, arg2)

def strategy_addition(arg1, arg2):
    return arg1 + arg2

def strategy_subtraction(arg1, arg2):
    return arg1 - arg2

def main():
    print("no_strategy", executor(4, 6))
    print("addition_strategy", executor(4, 6, strategy_addition))
    print("subtraction_strategy", executor(4, 6, strategy_subtraction))


if __name__ == '__main__':
    main()