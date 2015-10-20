'''
Name:Ranbir Dixit
Program: Mean_Median_Mode
Version:1
Description: Calculate the mean, median and mode of a list of numbers
'''
#import random
#numbers = list(random.range())
sum_numbers = 0
count = 0
count_numbers=0
numbers = [2,22,2,3,3]
sorted_numbers = sorted(numbers)
#calculating mean of elements in the list
for number in numbers:
    sum_numbers += number
    count +=1
    mean = sum_numbers/count
print "mean:",mean
#calculating the median of elements in the list
if count%2==0:
    midpoint1 = (count/2)-1
    midpoint2= count/2
    median = (sorted_numbers[midpoint1]+sorted_numbers[midpoint2])/2
    print "median:",median
else:
    midpoint = count/2
    median = sorted_numbers [midpoint]
    print "median:",median
#calculating the mode of the elements in the list
modedict={}
for number in sorted_numbers:
    #counts the occurrences of the sorted numbers
    count=sorted_numbers.count(number)
    #if the number is not in the dictionary add it to it
    if number not in modedict.keys():
        modedict[number]=count
    max_item=None
    max_count=0
#iterates through each key,value pair and updates the max_item and max_count variables as needed
for k,v in modedict.items():
    if v > max_count:
        max_item = k
        max_count = v
        print max_count
#print "mode dict values",modedict.items()
#print "mode dict keys",modedict.keys()
#print "mode dict values",modedict.values()
#print "mode dict values count max count",modedict.values().count(max_count)
#checks to see if there is a mode; that is, that not all values appear only once
if max_count == 1:
    print "all values appear once"
#checks to see if there are multiple modes by counting tgh
elif modedict.values().count(max_count)>1 :
    print "mode has multiple values"
else:
    print "mode:",max_item
    
    

    

     






