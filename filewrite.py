from os import path

adr = path.dirname(__file__)
file_haldler = open(adr +'/myfile.txt', 'w')


file_haldler.write("Hallo Wolt!")

file_haldler.close()

print(__file__)

with open ('yourfile.txt','a') as file:
    c = ord('a')
    while chr(c) != 'z':
        c += 1
        file.write(chr(c))
    file.close()
