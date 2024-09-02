#count
#sorted methods
#reverse methods
#clear methods
#copy methods

fruits = ['orange', 'apple', 'pears','banana','kiwi', 'apple']

print(fruits.count('apple')) #count the number of 'apple' in the list
fruits.sort()
print(fruits) #sort the list in ascending order
fruits.reverse()
print(fruits) #reverse the list

fruits_copy = fruits.copy() #copy the list
print(fruits_copy)


 #clear all elements in the list
fruits.clear()
print(fruits) #print the cleared list

