# Simple OOP Calculator
# Create methods for the Calculator class that can do the following:

# Add two numbers.
# Subtract two numbers.
# Multiply two numbers.
# Divide two numbers.
# Examples
# calculator = Calculator()

# calculator.add(10, 5) ➞ 15

# calculator.subtract(10, 5) ➞ 5

# calculator.multiply(10, 5) ➞ 50

# calculator.divide(10, 5) ➞ 2
# Notes
# The methods should return the result of the calculation.
# Don't worry about needing to handle division by zero errors.
# See the Resources tab for some helpful tutorials on Python classes.

#solution
class calculator:
    def __init__(self,firstNumber,secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber
    def add(self):
        return round(self.firstNumber + self.secondNumber,3)
    def multiply(self):
        return round(self.firstNumber * self.secondNumber,3)
    def divide(self):
        return round(self.firstNumber / self.secondNumber,3)
    def subtract(self):
        return round(self.firstNumber - self.secondNumber,3)

op = calculator(2,22).divide()
print(op)