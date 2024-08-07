#strings = ('Apple Banana Carrot').split()
strings = input("Enter a string: ").split()
vowel = ("a e i o u").split()
a = ""
result = []
ga = []
for item in strings:
    a = a + item

for item in a.lower():
    if item not in vowel and item not in result and item.isalpha():
        result.append(item)
    elif item in vowel and item not in ga:
        ga.append(item)

print(f"Unique vowels:  {ga}")
print(f"Unique consonants:  {result}")
