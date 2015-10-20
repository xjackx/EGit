'''
Name:Ranbir Dixit
Program: Dictreader CSV
Version:3
Description: uses DictReader to open a csv file and loop over all the rows and prints them out
'''
import csv
with open('C:\\Users\\rkd\\Desktop\\ITNPBD2\\lab-fileio-regex.csv') as f:
    r=csv.DictReader(f,delimiter=',')
    for line in r:
        print line 