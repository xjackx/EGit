'''
Name:Ranbir Dixit
Program: Dictreader CSV
Version:10
Description: uses DictReader to open a csv file and loop over all the rows to display only the names of people starting in AX and prints this out to file
'''
import csv
import re
with open("C:\\Users\\rkd\\Desktop\\ITNPBD2\\lab-fileio-regex.csv")as f:
    r=csv.DictReader(f,delimiter=",")
    for line in r:
        if re.search("AX.",line['Room']):
            with open("C:\\Users\\rkd\\Desktop\\ITNPBD2\\AX.txt",'w') as g:
                #print type(line)
                g.write(str(line))
            
            