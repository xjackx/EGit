'''
Name:Ranbir Dixit
Program: Dictreader CSV
Version:5
Description: uses DictReader to open a csv file and loop over all the rows to display only the names of people with a parking space
'''
import csv
with open("C:\\Users\\rkd\\Desktop\\ITNPBD2\\lab-fileio-regex.csv")as f:
    r=csv.DictReader(f,delimiter=",")
    for line in r:
        if line['HasParkingSpace']=='y':
            print line
    