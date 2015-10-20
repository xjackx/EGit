'''
Name:Ranbir Dixit
Program: Dictreader CSV
Version:8
Description: uses DictReader to open a csv file and loop over all the rows to display rows that have '@' missing from email address field
'''
import csv
import re
with open("C:\\Users\\rkd\\Desktop\\ITNPBD2\\lab-fileio-regex.csv")as f:
    r=csv.DictReader(f,delimiter=",")
    for line in r:
        #print line
        if re.search('^(.(?!@))*$',line['PersonalEmail']):
            print line