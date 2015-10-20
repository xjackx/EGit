'''
Name:Ranbir Dixit
Program: String Comparison
Version:1
Description: Checks to see if reversing a string returns the same string by slicing the string in reverse as described on:
http://stackoverflow.com/questions/18686860/reverse-a-string-in-python-without-using-reversed-or-1
'''

user_string=raw_input("enter a string to test: ")
if user_string[::-1]==user_string:
    print "True"
else:
    print "False"
