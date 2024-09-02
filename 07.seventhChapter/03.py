# how to add data and delete from dictionary

# create a dictionary

my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# add a new key-value pair

my_dict['country'] = 'USA'

print(my_dict)

# delete a key-value pair

del my_dict['age']

print(my_dict)

# checking if a key exists in a dictionary

if 'name' in my_dict:
    print('Name is in the dictionary')
else:
    print('Name is not in the dictionary')


returnedValue = my_dict.pop('name')

print('Returned value:', returnedValue)

print(my_dict)

user =  my_dict.popitem()

print('Popped item:', user)

print(my_dict)