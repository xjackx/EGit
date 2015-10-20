'''
Name:Ranbir Dixit
Program: Dictreader CSV
Version:7
Description: uses DictReader to open a csv file and loop over all the rows to display rows that have years of service in text rather than numbers
'''
import csv
import re
with open("C:\\Users\\rkd\\Desktop\\ITNPBD2\\lab-fileio-regex.csv")as f:
    r=csv.DictReader(f,delimiter=",")
    for line in r:
        if re.search('[\D]',line['YearsOfService']):
            print line