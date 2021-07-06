import random

uCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lCase = "abcdefghijklmnopqrstuvwxyz"
n = "1234567890"
s = "!@#$%&?+-*/"

strg = uCase + lCase + n + s


i=1
while(i==1):
    j=1
    while(j==1):
        lenght = int(input("Enter with the password lenght [MAX 30 AND MIN 3] : "))
        if lenght <= 30 and lenght >= 3:
            j=0
        
    password = "".join(random.sample(strg, lenght))
    print("Your final password : " + password)

    opcao = input("Do you want to generate a new password? [Press any key for generate or E to exit] : ")
    if opcao == "e" or opcao == "E":
        print(opcao)
        i=0