'''
Name:Ranbir Dixit
Program: Balanced Brackets
Version:1
Description: Checks to see if there is an even number of brackets.
'''

user_string=raw_input("please enter an expression with brackets: ")
left_count = 0
right_count=0
for element in user_string:
    if element =="(":
        left_count+=1
    #print left_count
    if element ==")":
        right_count+=1
    #print right_count
if right_count-left_count>0:
    print "missing",right_count-left_count,"left brackets in string"
elif left_count-right_count>0:
    print "missing",left_count-right_count,"right brackets in string"
else:
    print "matching number of  right brackets found "