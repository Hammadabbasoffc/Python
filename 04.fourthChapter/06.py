word = input("Enter the word : ")

def isPalindrome(word):
    reverse = word[::-1]
    if word == reverse:
        print("This is palindrome")
    else:
        print("This is not palindrome")

isPalindrome(word)