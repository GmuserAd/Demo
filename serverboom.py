# Seven Boom!
# Create a function that takes an array of numbers and return "Boom!" if the digit 7 appears in the array. Otherwise, return "there is no 7 in the array".

# Examples
# sevenBoom([1, 2, 3, 4, 5, 6, 7]) ➞ "Boom!"
# // 7 contains the number seven.

# sevenBoom([8, 6, 33, 100]) ➞ "there is no 7 in the array"
# // None of the items contain 7 within them.

# sevenBoom([2, 55, 60, 97, 86]) ➞ "Boom!"
# // 97 contains the number seven.

# Notes
# N/A

_l = [1,1221,33,56232325,111122122313,2356565655,111111]
# _z = []
# for _ in _l:
#     _ =  [int(i) for i in str(_)]
#     _z.extend(_)
# print(_z)


def serverBoom(li):
    _z = []
    for _ in li:
        _ =  [int(i) for i in str(_)]
        if 7 in _:
            print("Boom!")

serverBoom(_l)