numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def evenOdd(number):
    even = []
    odd = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    return even, odd

even, odd = evenOdd(numbers)
combineList = [even, odd]
print(combineList)
   