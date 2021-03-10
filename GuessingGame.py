##GUESSING GAME###
##You have to guess a positive integer in 1 to 100.
##you have 7 guess' 
import random
n=random.randrange(1,100,1)
print("Number is successfully generated.Now Guess")
total_guess=7

while(total_guess > 0):
    x=int(input("Enter your Guess(1 to 100):"))
    total_guess-=1
    if x < n:
        print("Guess Big!")
    elif x > n:
        print("Guess Small!")
    else:
        print("WOW!,GENIUS!")
        print("you won!")
        quit()

print("Game Over!, The Number was :",n)