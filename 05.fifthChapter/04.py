# delete the data from the list

fruits = ['orange', 'Apple', 'pears','banana','kiwi']

fruits.pop()

print(fruits)

# the pop() method removes the last item from the list and returns it

# pop(index) method removes the item at the specified index from the list and returns it

fruits.pop(1)

print(fruits)

# del operator removes the item at the specified index from the list and returns it

del fruits[2]

print(fruits)

# remove() method removes the first occurrence of the specified item from the list

fruits.remove('Apple')

print(fruits)

# clear() method removes all items from the list

fruits.clear()

print(fruits)

# empty list
