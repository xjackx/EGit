'''
Name:Ranbir Dixit
Program: String Comparison
Version:2
Description: Checks to see if reversing a string returns the same string by creating a list and then appending entries as described on:
http://stackoverflow.com/questions/18686860/reverse-a-string-in-python-without-using-reversed-or-1
'''
user_string=raw_input("enter a string to test: ")
#create a list to store elements of a loop
word_list=[]
count=1
#iterate over elements across the length of a word and add them in reverse order to the list
for letters in range(count,len(user_string)+1):
    word_list.append(user_string[len(user_string)-count])
    count+=1
#print word_list
#change list to string using join method
word_list=''.join(word_list)
#print word_list
if word_list==user_string:
    print "True"
else:
    print "False"