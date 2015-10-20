'''
Name:Ranbir Dixit
Program: Birthday Problem
Version:2
Description: Simulates the birthday problem as found on (http://en.wikipedia.org/wiki/Birthday_problem).
Probability that two people in a room share a birthday in a year that is not leap resolved using monte carlo simulation
as described on http://interactivepython.org/courselib/static/everyday/2013/09/1_birthday.html
'''
import random
number_of_days=365
#generate a number of random guesses across trials
number_of_trials = 1000
class_size=23
common_birthdays=0
#generate guesses for birthdays in the year
for trial in range(number_of_trials):
    #store generated birthdays in a list
    birthday =[]
    for student in range(class_size):
        birthday.append(random.randrange(number_of_days))
#print birthday
#iterate over birthday list to find the number of common birthdays and update the counter
    common = False
    for days in birthday:
        if birthday.count(days)>1:
            common=True
    if common==True:
        common_birthdays+=1
    #print common_birthdays
    print birthday
print "probability of having a common birthday = ",common_birthdays/float(number_of_trials)



