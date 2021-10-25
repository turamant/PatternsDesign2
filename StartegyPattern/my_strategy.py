def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def power(x, y):
    return x ** y

'''class Calculator:
    def __init__(self, func=None):
        self.execute = func

    def calculator(self, *args):
        if self.execute is not None:
            return self.execute(*args)
        return "Not implemented"
s = Calculator(add)
p = Calculator(pow)
d = Calculator()
print(d.calculator(4, 6))
print(s.calculator(4, 6))
print(p.calculator(3, 2))
'''

def calculator(x, y, func=None):
    if func is not None:
        return func(x, y)
    return "Not implementented"

def main():
    result = calculator(3, 2, power)
    print(result)

if __name__ == '__main__':
    main()
