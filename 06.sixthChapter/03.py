#function returning the two values

def func(int1, int2):
    add = int1 + int2
    multiply = int1 * int2

    return add, multiply

# calling the function and storing the returned values in variables

print(3,4)

add, multiply = func(3,4)

print("Addition:", add)

print("Multiplication:", multiply)
