'''
Name:Ranbir Dixit
Program: Guessing Game
Version:2
Description: Computer generates random guesses to try and match inital guess, uses bisection search
'''
import random
initial_guess=random.randrange(0,100)
#computer_guess=random.randrange(0,100)
computer_guess=50
print "Initial Guess: ", initial_guess
number_of_guesses=10
low=0
high=100
count=1
for guess in range(number_of_guesses):
    if computer_guess==initial_guess:
        print "computer guess",computer_guess
        print"correct, I took",count,"tries"
        break
    elif computer_guess>initial_guess:
        high=computer_guess
        print "computer guess: ",computer_guess
        print "too high"
        computer_guess=(low+high)/2
        count+=1
    elif computer_guess<initial_guess:
        low=computer_guess
        print "computer guess: ",computer_guess
        print "too low"
        computer_guess=(low+high)/2
        count+=1