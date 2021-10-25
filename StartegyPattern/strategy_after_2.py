'''Этот шаблон проектирования удачно назван шаблоном стратегии, потому что он позволяет нам писать
код, который использует некоторую стратегию, выбираемую во время выполнения, не зная ничего о
стратегии, кроме того, что она следует некоторой сигнатуре выполнения.'''

class StrategyExecutor:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def execute(self, arg1, arg2):
        if self.strategy is None:
            print("Strategy not implemented...")
        else:
            self.strategy.execute(arg1, arg2)

class AdditionStrategy:
    def execute(self, arg1, arg2):
        print(arg1 + arg2)

class SubtractionStrategy:
    def execute(self, arg1, arg2):
        print(arg1 - arg2)

def main():
    no_strategy = StrategyExecutor()
    addition_strategy = StrategyExecutor(AdditionStrategy())
    subtraction_strategy = StrategyExecutor(SubtractionStrategy())
    no_strategy.execute(4, 6)
    addition_strategy.execute(4, 6)
    subtraction_strategy.execute(4, 6)

if __name__ == '__main__':
    main()

'''По крайней мере, мы разобрались с растянутым оператором if, а также с необходимостью обновлять функцию
исполнителя каждый раз, когда мы добавляем другую стратегию. Это хороший шаг в правильном
направлении. Наша система немного более разобщена, и каждая часть программы имеет дело только
с той частью выполнения, с которой она связана, не беспокоясь о других
элементах системы.'''