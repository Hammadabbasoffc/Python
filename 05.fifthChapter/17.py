numbersList = [1,2,3,[4,5,6],[7,8,9,9],2,3,4,5,]

def checkList(numberList):
    num = 0
    for li in numberList:
        
        if type(li) == list:
            num += 1 
    return num
            

print(checkList(numbersList))