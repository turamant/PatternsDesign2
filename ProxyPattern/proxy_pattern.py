import time
class RawCalculator:
    def fib(self, n):
        if n < 2:
            return 1
        return self.fib(n-2) + self.fib(n-1)

def memoize(fn):
    __cashe = {}
    def memoized(*args):
        key = (fn.__name__, args)
        if key in __cashe:
            return __cashe[key]

        __cashe[key] = fn(*args)
        return __cashe[key]
    return memoized

class CalculatorProxy:
    def __init__(self, target):
        self.target = target
        fib = getattr(self.target, 'fib')
        setattr(self.target, 'fib', memoize(fib))
    def __getattr__(self, name):
        return getattr(self.target, name)



if __name__=='__main__':
    calculator = CalculatorProxy(RawCalculator())
    start_time = time.time()
    fib_sequence = [calculator.fib(x) for x in range(0, 800)]
    end_time = time.time()

    print("Calculating the list of {} Fibonachi numbers took {} seconds".
          format(
        len(fib_sequence),
        end_time - start_time
    ))