import random

n = random.randrange(1,20)
flag = 0
chance = 5
while(chance>0):
    chance = chance-1
    guess = int(input("Guess a number between 1 to 20 : "))
    if(guess > n):
            print("Your number is greater")
    elif(guess<n):
            print("Your number is smaller")
            print("Try again!")    
    else:
        print("You won!")
        flag = 1
        break
if(flag == 0):
    print("You loose")


    
print("The number was : ",n)
        


