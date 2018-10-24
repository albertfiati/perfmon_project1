#!/usr/bin/env python

from optparse import OptionParser
import matplotlib.pyplot as plt
import numpy as np

D_CPU = 0.394
D_Disk = [0.0771, 0.1238, 0.0804, 0.235]
D_Disk_bal = sum(D_Disk)/4
R_prime = 0.0
R = 0.0
X = 0.0
Z = 0.0
USER_Max = 5

R_prime_i = [[0.0 for x in range(USER_Max)] for y in range(4)]
X_i = [[0.0 for x in range(USER_Max)] for y in range(4)]
Q_i = [[0.0 for x in range(USER_Max)] for y in range(4)]

def plotThroughPut():
	x = np.arange(0, USER_Max);
	
	y = np.array(X_i)
	print y

	for n in xrange(0, 4):
		plt.plot(x,y[n])

	plt.xlabel('No of downloads')
	plt.ylabel('Throughput')
	plt.show()
	

def performComputations():
	for disk in xrange(0,len(D_Disk)):
		for n in xrange(1,USER_Max):
			R_prime_i[disk][n] = round(D_Disk[disk] * (1 + Q_i[disk][n-1]),3)
			#print "Rprime - " + str(R_prime_i[disk][n]);
			X_i[disk][n] = round(n / (Z + R_prime_i[disk][n]),3)
			#print "Xi - " + str(X_i[disk][n]);
			Q_i[disk][n] = R_prime_i[disk][n]*X_i[disk][n]
			#print Q_i[disk][n];

	plotThroughPut()
			

def computeResidenceTimeOfNode():
	print "residence time of node"

def sumOfResidenceTime():
	print "Sum of residence time is --"

def computeThroughputOfNode():
	print "throughput of node"

def sumOfThroughput():
	print "Sum of throughput is --"

def question1():
	print 'Solver for question 1'
	print

	performComputations();

	print

def question2():
	print 'Solver for question 2'
	print D_Disk_bal

def question3():
	print 'Solver for question 3'

def question4():
	print 'Solver for question 4'

def question5():
	print 'Solver for question 5'
	print USER_Max

def question6():
	print 'Solver for question 6'

def setMaxNoOfUsers(option, opt_str, value, parser):
	print "No of users " + str(value)
	USER_Max = value;
	

def execute(option, opt_str, value, parser):
	question = int(value)

	switcher ={
		1: question1,
		2: question2,
		3: question3,
		4: question4,
		5: question5,
		6: question6,
	}

	executer = switcher.get(question, lambda: "Invalid question number");
	executer();

def main():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")

    parser.add_option("-u", "--users",
    				  dest= 'users_max',
    				  type= 'int',
    				  action="callback",
                      callback=setMaxNoOfUsers,
                      help="Set the maximun number of users",)

    parser.add_option("-q", "--question",
    				  type= 'choice',
    				  dest= 'question_number',
    				  choices= ["1","2","3","4","5","6"],
                      action="callback",
                      callback=execute,
                      help="Select solver for a question number",)

    (options, args) = parser.parse_args()

if __name__ == '__main__':
    main()