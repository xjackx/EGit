'''
Program: number input
Ranbir Dixit
ver 1
last edit: 24_09_2015
'''

#input exception handling
while True:
    try:
            number = int(raw_input('please enter a number'))
            # return output based on the value of number
            if number<10:
                print "number is small"

            elif number>=10 and number<=20:
                print "number is medium"
	    else:
                print "number is large"
		#return even or odd based on value of integer
	    if number%2 == 0:
                print "number is even"
            else:
                print "number is odd"
            break
	except:
		number = int(raw_input('please enter a number'))
	
