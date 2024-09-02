# update method in dictionary

userInfo = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'email': 'john@example.com',
    'phone': '1234567890',
    'address': {
        'street': '123 Main St',
        'city': 'New York',
        'state': 'NY',
        'zip': '10001'
        }
}

moroInfo = { 'addressTwo': {'street': '123 Main Street','city': 'New York'}}

userInfo.update(moroInfo)

print(userInfo)