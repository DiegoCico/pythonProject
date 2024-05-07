alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(t, s):
    word = ""
    for i in t:
        p = alphabet.index(i)
        ns = p + s
        word += alphabet[ns]
    print(word)

def decode(t,s):
    word =""
    for i in t:
        p = alphabet.index(i)
        ns = p - s
        word += alphabet[ns]
    print(word)


if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decode(text,shift)