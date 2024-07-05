num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))


def greater(num1, num2):
    if num1 > num2:
        print("num1 is greater")
    else:
        print("Num2 is grater")


def newGreatest(num1, num2, num3):
    bigger = greater(num1, num2)
    return greater(bigger, num3)