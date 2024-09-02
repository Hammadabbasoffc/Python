stringList = ['abc','tuv','xyz']


def reverseStringList(list):
    for i in range(len(list)):
        list[i] = list[i][::-1]
    return list

reversedList = reverseStringList(stringList)

print(reversedList)