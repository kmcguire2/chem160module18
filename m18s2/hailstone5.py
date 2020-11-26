#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import sys

#correct input is the name of the script and the starting value
if len(sys.argv) != 2: 
	sys.exit("Program takes one argument, N") #exit with warning

#if the first value is not a number
if not sys.argv[1].isnumeric():
	sys.exit("Argument must be unsigned integer") #exit with warning

#if the tests are passed, assign N to the integer value of the first argument
N = int(sys.argv[1])

steps = 0
while N != 1:
	print(N)
	steps += 1
	if N%2 == 0:
		N = N//2
	else:
		N = 3*N+1
print("steps=", steps)
