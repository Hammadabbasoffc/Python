name = input('Enter the name : ')

i = 0
temp_var = ""
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")

    i +=1