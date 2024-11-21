class Calculator:
    def __init__(self) -> None:
        pass    

    def add(self, *values) -> float:
        sum = 0
        for x in values:
            sum += x
        return sum

    def subtract(self, num1, num2) -> float:
        return num1 - num2
    
    def multiply(self, *values) -> float:
        product = 1
        for x in values:
            product *= x
        return product
    
    #Hin
    def divide(self, num1, num2) -> float:
        return num1 / num2

calc = Calculator()

print(calc.add(2, 3))
print(calc.subtract(2, 3))
print(calc.multiply(2, 3))
try:
    n = calc.divide(2, 3)
except ZeroDivisionError as e:
    n =  f'Error: {e}'
print(n)
print(calc.add(calc.multiply(2, 3),calc.multiply(2, 3)))

