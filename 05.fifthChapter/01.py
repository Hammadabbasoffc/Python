# intro to list in python


numbers = [1,2,3,4  ,5,6,7,8,]
print(numbers)

words = ["word1", "word2", "word3", "word4"]
print(words)


mixed = [1,2,3,4,5,6,7,"word1", "word2",2.4,1.2,None]

print(mixed)

# accessing elements in a list

print(numbers[0])

print(words[3])

print(mixed[5])

# list slicing

print(numbers[1:3])

print(words[1:])

print(mixed[1:4:2])

# updating elements in a list

numbers[0] = 100

print(numbers)

mixed[5] = "updated_word"

print(mixed)