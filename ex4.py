# coding: utf-8
cars = 100           #定义变量cars,并赋值100
space_in_a_car = 4   #定义变量space_in_a_car,并赋值4
drivers = 30         #定义变量drivers,并赋值30
passengers = 90      #定义变量passengers,并赋值90
cars_not_driven = cars - drivers #定义变量cars_not_driven,并把cars与drivers的差值赋值给变量
cars_driven = drivers            #定义变量cars_driven,并把drivers的值赋值给变量
carpool_capacity = cars_driven*space_in_a_car          #定义变量carpool_capacity,并把cars_driven与space_in_a_car的乘积赋值给变量
average_passengers_per_car = passengers / cars_driven  #定义变量average_passengers_per_car，并把passengers与cars_driven的商赋值给变量


print "There are",cars, "cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about", average_passengers_per_car,"in each car."


i=16
j=21.5
x=0.8
y=(j-i)*x
print u"今天剩余的学习时间大概是",y