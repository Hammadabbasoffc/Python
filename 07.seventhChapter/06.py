
def cubeFinder(number):
    temDic = {}
    for i in range(number):
        cube = i ** 3
        temDic[i] = cube
    return temDic

print(cubeFinder(10))