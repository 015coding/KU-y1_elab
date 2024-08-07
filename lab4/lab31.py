def spel(x,shift):
    encrypt = []
    for char in x:
        if char.isalpha():
            if char.islower():
                start = ord('a')
            else:
                start = ord("A")
            shifted = (ord(char) - start + shift) % 26 + start
            encrypt.append(chr(shifted))
        else:

            encrypt.append(char)

    return ''.join(encrypt)


x = input("Enter text: ")
shift = int(input("Enter step: "))
print(spel(x,shift))