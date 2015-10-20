'''
Name:Ranbir Dixit
Program: Dictreader CSV
Version:2
Description: uses DictReader to open a csv file and prints the number of columns and rows to the screen
'''
import csv
column_count=0
with open('C:\\Users\\rkd\\Desktop\\ITNPBD2\\lab-fileio-regex.csv') as f:
    r=csv.DictReader(f,delimiter=',')
    line_count=1 #initialize at 1 as counting starts from 0
    for line in r:
        line_count+=1
    print "number of rows: ", line_count
    print "number of columns:", len(r.fieldnames)