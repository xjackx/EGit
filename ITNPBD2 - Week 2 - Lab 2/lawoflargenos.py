'''
Name:Ranbir Dixit
Program: Law of Large Nos.
Version:1
Description: generates sample statistics based on different sample sizes in order to prove that as the number of samples drawn approaches infinity the sample statistic approaches the expected value
https://en.wikipedia.org/wiki/Law_of_large_numbers
'''
import random
from numpy import mean, median, min, max,std

from scipy.stats import mode

#def mode(x):
    #return max(set(x), key=x.count)

sample_size1=10
sample_size2=100
sample_size3=1000
sample_size4=10000
population_size=10000
#generate a population list
population_list=[]
for numbers in range(population_size):
    population_list.append(random.randrange(100))
print len(population_list)

#generate sample size lists, sampling from population list
sample_list1=[random.sample(population_list,sample_size1) for numbers in range(sample_size1)]
#print sample_list1
#print len(sample_list1)

sample_list2=[random.sample(population_list,sample_size2) for numbers in range(sample_size2)]
#print sample_list2
#print len(sample_list2)

sample_list3=[random.sample(population_list,sample_size3) for numbers in range(sample_size3)]
#print sample_list3
#print len(sample_list3)

sample_list4=[random.sample(population_list,sample_size4)for numbers in range(sample_size4)]
#print sample_list4
#print len(sample_list4)

print "the population mean is: ",mean(population_list),"\n","sample size 1 mean is: ",mean(sample_list1),"\n","sample size 2 mean is: ",mean(sample_list2),"\n",\
"sample size 3 mean is: ", mean(sample_list3),"\n","sample size 4 mean is: ",mean(sample_list4)

print "the population median is: ",median(population_list),"\n","sample size 1 median is: ",median(sample_list1),"\n","sample size 2 median is: ",median(sample_list2),"\n",\
"sample size 3 median is: ", mean(sample_list3),"\n","sample size 4 median is: ",median(sample_list4)

print "the population mode is: ",mode(population_list),"\n","sample size 1 mode is: ",mode(sample_list1),"\n","sample size 2 mean is: ",mode(sample_list2),"\n",\
"sample size 3 mean is: ", mode(sample_list3),"\n","sample size 4 mode is: ",mode(sample_list4)

print "the population min is: ",min(population_list),"\n","sample size 1 min is: ",min(sample_list1),"\n","sample size 2 min is: ",min(sample_list2),"\n",\
"sample size 3 min is: ", min(sample_list3),"\n","sample size 4 min is: ",min(sample_list4)

print "the population max is: ",max(population_list),"\n","sample size 1 max is: ",max(sample_list1),"\n","sample size 2 max is: ",max(sample_list2),"\n",\
"sample size 3 max is: ", max(sample_list3),"\n","sample size 4 max is: ",max(sample_list4)

print "the population sd is: ",std(population_list),"\n","sample size 1 sd is: ",std(sample_list1,ddof=1),"\n","sample size 2 sd is: ",std(sample_list2,ddof=1),"\n",\
"sample size 3 sd is: ", std(sample_list3,ddof=1),"\n","sample size 4 sd is: ",std(sample_list4,ddof=1)