name = 'Zad A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180 #  lbs
eyes = 'Blue' 
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s."  % name
print "He's %d centimeters tall."  % (2.54 * height)
print "He's %g kilograms heavy." % (0.4536 * weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair."  % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d."  % (age, height, weight, age + height + weight)

text = "I am %d years old."  % 22
print "I said: %s." % text
print "I said: %r." % text

import datetime
d = datetime.date.today()
print "%s" % d
print "%r" % d
