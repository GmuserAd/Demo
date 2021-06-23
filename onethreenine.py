# Given an int, figure out how many ones, threes and nines you could fit into the number. 
# You must create a class. You will make variables (class.ones, class.threes, class.nines) to do this.

# Examples
# let n1 = new OnesThreesNines(5)
# n1.nines ➞ 0
# n1.ones ➞ 5
# n1.threes ➞ 1

class OneTreeNine:
    def __init__(self,number):
        self.number = number
        self.ones = number
        self.threes = int(number/3)
        self.nines = int(number/9)

#test


n1 = OneTreeNine(500000)

print(n1.ones)
print(n1.threes)
print(n1.nines)
