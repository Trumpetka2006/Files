import unicodedata as unc
from sys import stdout, stdin

while True:
    try:
        path = input("File path ->")
        file = open(path, "r")
    except FileNotFoundError:
        print("File dont Exist!")
    else: break
mode = input("Select mode [co/de] ->")
while True:
    try:
        key = int(input("Set code key ->"))
    except: print("Key MUST be a number!")
    else:break

#fileIn = open(path, "r")

def string_shift(text: str, key: int):
    resolut = ""
    text = unc.normalize("NFKD",text).encode("ascii", "ignore").decode("ascii")
    text = text.upper()
    for char in text:
        position = ord(char) -65
        position += key
        position = position % 26
        resolut += chr(position +65)
    return resolut  


if(mode == "co"):
    fileIn = open(path, "r")
    cache = fileIn.read()
    fileIn.close()
    fileOut = open(path, "w")
    fileOut.write(string_shift(cache, key))
    fileOut.close()
    cache = None

if(mode == "de"):
    fileIn = open(path, "r")
    cache = fileIn.read()
    fileIn.close()
    fileOut = open(path, "w")
    fileOut.write(string_shift(cache, -key))
    fileOut.close()
    cache = None
#print(string_shift(fileIn.read(), key))
