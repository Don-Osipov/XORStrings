import sys

mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()[
    :-1
]  # removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[
    :-1
]  # removes the mandatory \n at the end of the file to support one line messages.
debug = False

if debug:
    print("mode:" + mode)
    print("key: " + key)
    print("inp: " + inp)


def elongateKeytext(keytext, text):
    if len(keytext) == len(text):
        return keytext

    targetLength = len(text)
    newKeyText = ""

    while len(newKeyText) < targetLength:
        for letter in keytext:
            newKeyText += letter
            if len(newKeyText) >= targetLength:
                break

    return newKeyText


key = elongateKeytext(key, inp)


def stringToInt(text):
    intList = []
    for char in text:
        intList.append(ord(char))

    return intList


def XORing(text, key):
    textInts = stringToInt(text)
    keyInts = stringToInt(key)
    output = ""

    for x, y in zip(textInts, keyInts):
        output += chr(x ^ y)

    return output


print(inp)
print(stringToInt(inp))
print(key)
print(stringToInt(key))

print(XORing(inp, key))
