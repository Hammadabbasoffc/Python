userInfo = {
    "Name": "John Doe",
    "Age": 30,
    "City": "New York",
    'favMovies': ['tito pati', 'hello world', 'hehie']
}

if 'Name' in userInfo:
    print(f"{userInfo['Name']} is present")


#looping in dictionary

for key, value in userInfo.items():
    print(f"{key} : {value}")

print(userInfo.items())