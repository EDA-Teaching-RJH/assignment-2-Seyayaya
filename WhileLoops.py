### Part Two -- your code goes here. 
import random

#random.int()
answer = random.randint(1,100)
guess = int(input("Please guess a number between 1-100\n"))

while guess != answer:
    guess = int(input("Sorry, That's the wrong answer, please try again\n"))
print("That's Correct. Well done!")
    