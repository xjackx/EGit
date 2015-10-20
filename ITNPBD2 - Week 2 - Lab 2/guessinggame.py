'''
Program: Guessing Game
Ranbir Dixit
ver 1
last edit: 24_09_2015
'''
count = 0
import random
number = random.randint(0,100)
#print 'number: ', number

#exception handling
while True:
    try:
        guess = int(raw_input('Please guess a number: '))
        count+=1
        if guess == number:
            print 'correct'
            break
        elif guess > number:
            print 'too high'
            #guess = int(raw_input('Please guess a number: '))
        elif guess<number:
            print 'too low'
            #guess = int(raw_input('Please guess a number: '))
        #break
    except:
        print "not an integer"
        #guess = int(raw_input('Please guess a number: '))
print 'you took ',count,'attempts!'
    
        
    