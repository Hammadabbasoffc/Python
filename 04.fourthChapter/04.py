num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

def greatest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print("First number is greater")
    elif num2 > num1 and num2 > num3:
        print("Second number is grater")
    else:
        print("Third number is grater")


greatest(num1, num2, num3)

