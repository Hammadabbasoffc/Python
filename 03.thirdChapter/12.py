num = input("Enter the number : ")


i = 0
total = 0

numLen = len(num)
print(numLen)

while i < numLen:
    total = total + int(num[i])
    i+=1

print(total)