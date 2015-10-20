'''
Name:Ranbir Dixit
Program: Guessing Game
Version:3
Description: Computer generates random guesses to try and match initial random guess
'''
import random
initial_guess=random.randrange(0,100)
computer_guess=random.randrange(0,100)
print "Initial Guess:",initial_guess
number_of_guesses=10
count=1
for guess in range(number_of_guesses):
    if computer_guess==initial_guess:
        print"correct, I took",count,"guesses"
        break
    elif computer_guess>initial_guess:
        print "computer guess: ",computer_guess
        print "too high"
        computer_guess-=1
        count+=1
    elif computer_guess<initial_guess:
        print "computer guess: ",computer_guess
        print "too low"
        computer_guess+=1
        count+=1
