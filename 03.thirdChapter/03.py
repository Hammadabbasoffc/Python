winning_number = 4
guess_number = int(input("Enter the number: "))

if winning_number == guess_number:
    print("Congo you Win the race")
elif winning_number < guess_number :
    print("Your Entered the higher value")

else:
    print("The number is to low")
