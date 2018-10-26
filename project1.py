#!/usr/bin/env python

from optparse import OptionParser
import matplotlib.pyplot as plt
import numpy as np 


#Global variables used in the solvers
LEGENDS = ["CPU","Disk_1","Disk_2","Disk_3","Disk_4"]			# The legend titles
D = [0.0394, 0.0771, 0.1238, 0.0804, 0.235]						# Service demand for all nodes
question = 1													# The question to solve
N = 120															# The number of concurrent downloads
Z = 0															# The wait time of the system

U = [0.0 for x in range(N)]										# Utilization of the system for all N
R = [0.0 for x in range(N)]										# Response time of the system for all N							
X = [0.0 for x in range(N)]										# Throughput of the system for all N
RPrime = [0.0 for x in range(N)]								# Residence time of the system for all N

sumRprime = [0.0 for x in range(N)]								# Summation of RPrime for all N

Ui = [[0.0 for x in range(N)] for y in range(len(D))]			# Utilization of all disks for all N
Ri = [[0.0 for x in range(N)] for y in range(len(D))]			# Response time of all disks for all N
Xi = [[0.0 for x in range(N)] for y in range(len(D))]			# Throughput of all disks for all N
Qi = [[0.0 for x in range(N)] for y in range(len(D))]			# Queue length of all disks for all N
RPrimei = [[0.0 for x in range(N)] for y in range(len(D))]		# Residence time of all disks for all N


# main method to parse options and then execute the solver
def main():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")

    parser.add_option("-d", "--downloads",
    				  dest= 'max_concurrent_downloads',
    				  type= 'int',
    				  action="callback",
                      callback=setN,
                      help="Set the maximun number of concurrent downloads")

    parser.add_option("-q", "--question",
    				  type= 'choice',
    				  dest= 'question_number',
    				  choices= ["1","2","3","4","5","6"],
                      action="callback",
                      callback=chooseExecuter,
                      help="Select solver for a question number")

    parser.add_option("-z", "--think-time",
    				  type= 'int',
    				  dest= 'think_time',
                      action="callback",
                      callback=setZ,
                      help="Set the think time")

    (options, args) = parser.parse_args()

    print
    print "*************************************"
    print
    print " Think time: " + str(Z)
    print " Question number: " + str(question)
    print " Max oncurrent downloads: " + str(N)
    print
    print "*************************************"
    print

    updateArrays()
    execute()
    

# set the number of concurrent donwloads based on parsed options
def setN(option, opt_str, value, parser):
	global N
	N = value;


# set the think based on parsed options
def setZ(option, opt_str, value, parser):
	global Z
	Z = value;


# change the defualt solver pased on the option parsed
def chooseExecuter(option, opt_str, value, parser):
	global question
	question = int(value)


def updateArrays():
	global U
	global R
	global X
	global RPrime
	global sumRprime
	global Ui
	global Ri
	global Xi
	global Qi
	global RPrimei

	U = [0.0 for x in range(N)]										# Utilization of the system for all N
	R = [0.0 for x in range(N)]										# Response time of the system for all N							
	X = [0.0 for x in range(N)]										# Throughput of the system for all N
	RPrime = [0.0 for x in range(N)]								# Residence time of the system for all N

	sumRprime = [0.0 for x in range(N)]								# Summation of RPrime for all N

	Ui = [[0.0 for x in range(N)] for y in range(len(D))]			# Utilization of all disks for all N
	Ri = [[0.0 for x in range(N)] for y in range(len(D))]			# Response time of all disks for all N
	Xi = [[0.0 for x in range(N)] for y in range(len(D))]			# Throughput of all disks for all N
	Qi = [[0.0 for x in range(N)] for y in range(len(D))]			# Queue length of all disks for all N
	RPrimei = [[0.0 for x in range(N)] for y in range(len(D))]		# Residence time of all disks for all N


# execute a particular solver
def execute():
	switcher ={
		1: question1,
		2: question2,
		3: question3,
		4: question4,
		5: question5,
		6: question6,
	}

	executer = switcher.get(question, lambda: "Invalid question number")
	executer()


# solver for question 1
def question1():
	print 'Solver for question 1'
	
	performComputations()
	
	x = np.arange(0, N)
	y = np.array(Ui)
	z = np.array(U)

	for disk in xrange(0,len(y)):
		plt.plot(x, y[disk], label=LEGENDS[disk], linewidth=2)

	#plt.plot(x, z, label='System', linewidth=2)
	
	plt.xlabel('No of concurrent downloads')
	plt.ylabel('Utilization')
	plt.grid(True)
	plt.legend()
	plt.show()	


#solver for question 2
def question2():
	print 'Solver for question 2'
	performComputations()
	
	x = np.arange(0, N)
	y = np.array(RPrimei)
	z = np.array(R)
	sla_y = np.array([20.0 for i in range(N)])

	for disk in xrange(0,len(y)):
		plt.plot(x, y[disk], label=LEGENDS[disk], linewidth=2)

	#plt.plot(x, z, label='System', linewidth=2)	
	plt.plot(x, sla_y, label='SLA', linewidth=2)

	plt.xlabel('No of concurrent downloads')
	plt.ylabel('Response time')
	plt.grid(True)
	plt.legend()
	plt.show()


# solver for question 3
def question3():
	print 'Solver for question 3'
	
	Dbal = (D[1]+D[2]+D[3]+D[4])/4
	D[1] = Dbal
	D[2] = Dbal
	D[3] = Dbal
	D[4] = Dbal
	performComputations()

	x = np.arange(0, N)
	y = np.array(Ui)
	z = np.array(R)
	sla_y = np.array([20.0 for i in range(N)])

	for disk in xrange(0,len(y)):
		plt.plot(x, y[disk], label=LEGENDS[disk], linewidth=2)

	#plt.plot(x, z, label='System', linewidth=2)	
	plt.plot(x, sla_y, label='SLA', linewidth=2)

	plt.xlabel('No of concurrent downloads')
	plt.ylabel('Utilization')
	plt.grid(True)
	plt.legend()
	plt.show()


# solver for question 4
def question4():
	print 'Solver for question 4'


# solver for question 5
def question5():
	print 'Solver for question 5'
	
	D[0] = 0.137

	Dbal = (D[1]+D[2]+D[3]+D[4])/4
	D[1] = Dbal
	D[2] = Dbal
	D[3] = Dbal
	D[4] = Dbal

	performComputations()

	x = np.arange(0, N)
	y = np.array(RPrimei)
	sla_y = np.array([20.0 for i in range(N)])

	for disk in xrange(0,len(y)):
		plt.plot(x, y[disk], label=LEGENDS[disk], linewidth=2)

	plt.plot(x, sla_y, label='SLA', linewidth=2)

	plt.xlabel('No of concurrent downloads')
	plt.ylabel('Response time')
	plt.grid(True)
	plt.legend()
	plt.show()


#solver for question 6
def question6():
	print 'Solver for question 6'
	
	Dbal = (D[1]+D[2]+D[3]+D[4])/4
	D[1] = Dbal
	D[2] = Dbal
	D[3] = Dbal
	D[4] = Dbal

	performComputations()

	x = np.arange(0, N)
	y = np.array(RPrimei)
	z = np.array(R)
	sla_y = np.array([20.0 for i in range(N)])

	for disk in xrange(0,len(y)):
		plt.plot(x, y[disk], label=LEGENDS[disk], linewidth=2)

	plt.plot(x, z, label='System', linewidth=2)
	plt.plot(x, sla_y, label='SLA', linewidth=2)

	plt.xlabel('No of concurrent downloads')
	plt.ylabel('Response time')
	plt.grid(True)
	plt.legend()
	plt.show()


#run computations using the closed and open model
def performComputations():
	print

	for n in xrange(1,N):
		for i in xrange(0,len(D)):	
			RPrimei[i][n] = D[i] * (1 + Qi[i][n-1])
			sumRprime[n] += RPrimei[i][n]

		X[n] = n / (Z + sumRprime[n])
		
		for i in xrange(0,len(D)):
			Qi[i][n] = RPrimei[i][n] * X[n]
			Ui[i][n] = X[n] * D[i] * 100
			Ri[i][n] = D[i]/(1.0-(Ui[i][n]*0.01))

			U[n] += Ui[i][n]
			R[n] += RPrimei[i][n]


#call main function
if __name__ == '__main__':
    main()

