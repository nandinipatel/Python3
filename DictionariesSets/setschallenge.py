text = input("Please enter some text: ").lower()

vowels = frozenset("aeiou")

char = set(text).difference(vowels)
print(char)

charSorted = sorted(char)
print(charSorted)