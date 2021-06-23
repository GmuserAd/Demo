import random
import string


def passwordGen():
    letters = string.ascii_letters+ string.punctuation + string.digits
    password = ''.join(random.choice(letters) for i in range(1,15))
    return password

print(passwordGen())
