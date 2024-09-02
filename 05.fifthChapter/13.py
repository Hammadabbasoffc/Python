number = [0, 1, 2, 3, 4, 5]

def reverse(list):
    emptyList = []
    for i in range(len(list)):
        lastValue = list.pop()
        emptyList.append(lastValue)

    return emptyList

print(reverse(number))