
import random as r

compNum = r.randint(1,100)
print(f"Computer number {compNum}!")

count = 1
while True:
    userGuess = int(input("Guess the numer between 1 to 100: "))
    try 

    if userGuess<compNum:
        print("Higher number please\n")
        count +=1
    elif userGuess>compNum:
        print("lower number please.\n")
        count +=1
    elif userGuess==compNum:
        print(f"You Guess matched with mine and you  took {count} attemps  to guess number correctly\n")
        break

    
        