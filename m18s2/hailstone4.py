#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
N = int(input("Enter starting value:"))
steps = 0
while N != 1:
	print(N)
	steps += 1
	if N%2 == 0:
		N = N//2
	else:
		N = 3*N+1
print("steps=", steps)
