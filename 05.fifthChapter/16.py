numberOne = [1, 2, 3, 4]
numberTwo = [1, 2, 6,7, 8, 9, 10, 11]


# def commonElements(list1, list2):
#     return list(set(list1) & set(list2))

# print(commonElements(numberOne, numberTwo))

def commonElements(numberOne, numberTwo):
    result = []
    for num in numberOne:
        if num in numberTwo:
            result.append(num)
    return result

print(commonElements(numberOne, numberTwo))
