# coding: utf-8
people = 30
cars = 40
buses = 15


if cars > people:    #判断车子的数量是否大于人的数量，大于就执行下面的语句，后面的以此类推
	print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."
	
if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."
	
if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
