#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import sys
print("I see ", len(sys.argv)," arguments") #print how many arguments we find
print("They are: ", sys.argv) #print each value
if sys.argv[1].isnumeric(): #test is the first value is numeric
	print("First arg is numeric: ", int(sys.argv[1]))
else:
	print("First arg is non-numeric")
