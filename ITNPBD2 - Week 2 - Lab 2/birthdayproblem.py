'''
Name:Ranbir Dixit
Program: Birthday Problem
Version:1
Description: Simulates the birthday problem as found on (http://en.wikipedia.org/wiki/Birthday_problem).
Probability that two people in a room share a birthday in a year that is not leap
'''
import math
#total number of people in room
number_in_room = 23
days_in_year=365
prob_no_bday=1.0

for people in range(number_in_room):
    #print "people in room: ",people+1
    prob_no_bday=prob_no_bday*(days_in_year-people)/365
    #print "probability of no birthday is: ", prob_no_bday
print "probability of no birthday is: ", prob_no_bday
#probability that two people share the same birthday P(B) =1-P(NB)
print "probability of a birthday is: ",1-prob_no_bday



