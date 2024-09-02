def wordCounter(word):
    count = {}

    for char in word:
        count[char] = word.count(char)

    return count

word = input("Enter a word: ")

result = wordCounter(word)

print(result)