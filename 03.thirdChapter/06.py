age = int(input("Enter Your Age: "))
if age >= 1 and age <= 3:
    print("Your Ticket Price is free ")
elif age >= 4 and age <= 10:
    print("Your Ticket Price is 150")
elif age >= 11 and age <= 60:
    print("Your ticket price is 200")
else:
    print("Your ticket price is 250")
