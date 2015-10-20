'''
Name:Ranbir Dixit
Program: Histograms of various generated distributions
Version:1
Description: generates a histogram based on various distributions - Gaussian, Uniform etc.
'''
from numpy import random
import matplotlib.pyplot as plt
exam_scores=random.randint(0,100,size=1000)
plt.hist(exam_scores,bins=10)
plt.title("exam scores histogram")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")
plt.show()