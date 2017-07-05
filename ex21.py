def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def substract(a, b):
	print "SUBSTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" %(a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" %(a, b)
	return a / b

def alg1(*args):
	a, b, c, d = args
	print "alg1: %d + %d / %d - %d" % (a, b, c, d)
	return a + b / c - d
	
print "Let's do some math with just functions!"

"""
age = input("input the age: ")
height = input("input the height: ")
weight = input("input the weight: ")
iq = input("input the iq: ")

age = add(age, 5)
height = substract(height, 4)
weight = multiply(weight, 2)
iq = divide(iq, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# a puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, substract(height, multiply(weight,divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"

"""
a = 24
b = 34
c = 100
d = 1023

result = alg1(a, b, c, d)
print "the result is: %d " % result
