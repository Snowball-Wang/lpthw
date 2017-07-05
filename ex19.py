def cheese_and_crackers(cheese_count, boxers_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxers_of_crackers
	print "Man that's enough for a party"
	print "Get a blanket.\n"
	
	
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)                          


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50                         #to show that parameters can be variables

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)                 #to show that parameters can be math expressions

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)  #display the results when parameters are math expression and variables
