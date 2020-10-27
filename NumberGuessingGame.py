import math
from random import randint

def randGenerator(minVal,maxVal):
    return  randint(minVal,maxVal)

def success():
  
        file = open("results.txt", "a+")
        file.write(name + " " + str(counter) + "\n")
        file.close()

def failure():
        print("Game Over!")
        print("The number wasn't guessed correctly in the allowed attempts. The number was", num)
        
if __name__=="__main__":
    counter = 0
    num = randGenerator(-100,100)
    
    print("Welcome to my game! This game only allows 10 guesses before the game terminates!")
    name = input("Enter name: ")
    
    guess = int(input("Guess a number:"))
    
    while num != guess and counter < 10:
            
        if num > guess:
            print("Low Guess")
            guess = int(input("Guess a number:"))
                              
        else:
            print("High Guess")
            guess = int(input("Guess a number:"))

        counter = counter + 1    
        if counter == 10:
            failure()
        
        if num == guess:
            print("Congrats you guess the number in less than 10 tries!")
            success()
            
            
