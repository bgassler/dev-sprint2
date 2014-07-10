# Enter your answrs for chapter 6 here
# Name: Brendan Gassler


# Ex. 6.6
def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]


"""1) If you call middle on a string of just 2 letters it 
returns the empty string. Same if it is called with a
string of one letter. Also the Same for the empty string"""

#number 2
def is_palindrome(word):
	length = len(word)
	if length == 1:
		#print 'True'
		return True
	elif length == 2:
		if last(word) == first(word):
			#print 'True'
			return True
		else:
			#print 'False'
			return False
	elif length >= 3 :
		if last(word) == first(word):
			is_palindrome(middle(word))
		else:
			#print 'False'
			return False


#print middle('hello')
is_palindrome('abcdefggfedcba')

# Ex 6.8
def gcd(a, b):
	if a > b:
		r = a % b
		gcd(b, r)
		print r
	elif b > a:
		r = b % a
		gcd(a, r)
		print r
	else:
		print a
		return a

gcd(9, 15)