import unicodedata as unc
import os
from sys import stdin

characters = {}
specialCharacters = {}
inputText = ""
resolut = [0,0,0] #délka textu, pocet znaků, pocet speciálních znaků

def character_set():
    for i in range(ord("a"), ord("z")+1):
        characters[chr(i)] = 0
    print(characters)
    for i in range(ord("A"), ord("Z")+1):
        characters[chr(i)] = 0

def analyze(data):
    

    for i in data:
        resolut[0] += 1
        i = unc.normalize("NFKD",i).encode("ascii", "ignore").decode("ascii")

        if i in characters:
            characters[i] += 1
            resolut[1] += 1
        else: 
            resolut[2] += 1 
            if i in specialCharacters:
                specialCharacters[i] += 1
            else: specialCharacters[i] = 1
            
def lsi():
    for i in characters:
         print(i)
def rat():
     for i in characters:
          if(characters[i] != 0):
                print(f"{i}: {characters[i]} {round(characters[i] / resolut[0],2) * 100}% |",end="")
                print("#" * int((round(characters[i] / resolut[0],1 )* 50)))
def cont():
    for i in characters:
         print(f"{i}: {characters[i]}")

def ex(seznam):
    nej = 0
    for i in seznam:
         if i > nej: nej = i
    print(nej)

character_set()
#inputText = input('Zadej text k analýze> ')
inputText = stdin.read()
analyze(inputText)
print("Analýza dokončena")
print(f">Počet znaků: {resolut[0]} \
       \n>Počet běžných znaků: {resolut[1]} \
       \n>Počet speciálních znaků: {resolut[2]}")

rat()
while False:
        #command = str(input("operation> "))
        command = "rat"
        if(command == "help"):
            print("ls -i \tshow input text\nls -a \tshow all defined characters")
            print("cont \tshow analyzed content")
            print("rat \tshow ratio of characters in input")
            print("find \tuse to find specific character")
            print("clr \tuse to clear console")
            print("ex \t show extreme characters")
            print("end \texit python")
        elif(command == "end"): break
        elif(command == "ls -i"): print(inputText)
        elif(command == "ls -a"): lsi()
        elif(command == "clr"): os.system('clear')
        elif(command == "rat"): rat()
        elif(command == "cont"): cont()
        elif(command == "ex"): ex(characters.values())

        
        
        
print("***SPECIÁLNÍ_ZNAKY***")
for i in specialCharacters:
        print(f"{i}: {specialCharacters[i]}")
