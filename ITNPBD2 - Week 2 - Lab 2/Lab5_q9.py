'''
Name:Ranbir Dixit
Program: Dictreader CSV
Version:9
Description: uses DictReader to open a csv file and loop over all the rows to display rows that have '.com' missing from email address field
'''
import csv
import re
with open("C:\\Users\\rkd\\Desktop\\ITNPBD2\\lab-fileio-regex.csv")as f:
    r=csv.DictReader(f,delimiter=",")
    for line in r:
        #print line
        #use negative look ahead re expression to exclude all missing .com
        if re.search('^(.(?!\.com))*$',line['PersonalEmail']):
            print line