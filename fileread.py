from sys import stdout, stdin


input = stdin.read(5)
print (input)

f = open ('myfile.txt', 'r')
char = f.read(1)
f.seek(0)
print()
print(f.read(512))
print(char)

f.close()