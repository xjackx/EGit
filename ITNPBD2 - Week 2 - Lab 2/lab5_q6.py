'''
Name:Ranbir Dixit
Program: Dictreader CSV
Version:6
Description: uses DictReader to open a csv file and loop over all the rows to display only the names of people starting in AX
'''
import csv
import re
with open("C:\\Users\\rkd\\Desktop\\ITNPBD2\\lab-fileio-regex.csv")as f:
    r=csv.DictReader(f,delimiter=",")
    for line in r:
        if re.search("AX.",line['Room']):
            print line['Room']