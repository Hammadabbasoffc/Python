
name , character = input("Enter Name and the character you want to find Comma seperated : ").split(",")
smallChar = character.lower()
smallName = name.lower()
print(f"Your Name Length is {len(name)} and in name {character} is present {smallName.count(smallChar)} Times")

