'''
Name:Ranbir Dixit
Program: Guessing Game
Version:1
Description: Computer generates random guesses to try and match initial random guess
'''
import random
initial_guess=random.randrange(0,100)
computer_guess=random.randrange(0,100)
print initial_guess
number_of_guesses=10
count=1
for guess in range(number_of_guesses):
    if computer_guess==initial_guess:
        print"correct, I took",count,"guesses"
        break
    elif computer_guess>initial_guess:
        print "too high"
        print "computer guess: ",computer_guess
        computer_guess=random.randrange(0,100)
        count+=1
    else:
        print "too low"
        print "computer guess: ",computer_guess
        computer_guess=random.randrange(0,100)
        count+=1


