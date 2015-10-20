'''
Name:Ranbir Dixit
Program: Dictreader CSV
Version:1
Description: uses DictReader to open a csv file and prints column headings to the screen
'''

import csv

with open('C:\\Users\\rkd\\Desktop\\ITNPBD2\\lab-fileio-regex.csv') as f:
    r=csv.DictReader(f,delimiter=',')
    print (r.fieldnames)