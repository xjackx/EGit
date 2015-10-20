'''
Name:Ranbir Dixit
Program: Birthday Problem
Version:1
Description: Simulates the birthday problem as found on (http://en.wikipedia.org/wiki/Birthday_problem).
Probability that two people in a room share a birthday in a year that is not leap
'''
import math
#total number of people in room
N=23

days_in_year=365

#probability that no two people share the same birthday P(NB) = (days_in_year-number of people+1)!/(days_in_year)!

prob_no_bday=math.factorial(days_in_year-N+1)/math.factorial(days_in_year)

print "probability that NO two people share the same birthday: ", prob_no_bday

#probability that two people share the same birthday P(B) =1-P(NB)

prob_bday=1-prob_no_bday

print "probability that two people share the same birthday: ", prob_bday

