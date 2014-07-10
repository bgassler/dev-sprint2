# Enter your answrs for chapter 7 here
# Name:


# Ex. 7.5
import math

def factorial(n):
	if n==0:
		return 1
	else:
		recursion  = factorial(n-1)
		num = n * recursion
		return num

def estimate_pi():
	total = 0
	iterations = 0
	k = 0
	factor = 2 * math.sqrt(2)/9801
	while True:
		numer  = factorial(4*k) * (1103 + 26390*k)
		denom = (factorial(k) ** 4) * (396 ** (4*k))
		term = factor * numer / denom
		total += term
		iterations += 1

		if abs(term) < 1e-15: break
		k += 1
	print "number of iterations: ", + iterations
	return 1 / total

print estimate_pi()

# How many iterations does it take to converge?
#it takes 3 iterations to converge