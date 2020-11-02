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

print(key)
print(inp)


def elongateKeytext(keytext, text):
    targetLength = len(text)
    newKeyText = ""

    while len(newKeyText) < targetLength:
        for letter in keytext:
            newKeyText += letter
            if len(newKeyText) >= targetLength:
                break

    return newKeyText
