# coding: utf-8
x = "There are %d types of people." % 10   #把字符串赋值给变量x
binary = "binary"                          #把binary这个字符赋值给binary这个变量
do_not = "don't"                           #把don't这个字符赋值给do_not这个变量
y = "Those who knows %s and those who %s." % (binary, do_not)    #把字符串赋值给变量y，赋值过程中调用binary和don't变量

print x      #打印变量x
print y      #打印变量y

print "I said: %r." % x         # %r表示输出Python所认为的原形
print "I also said: '%s'." % y

hilarious = False               #布尔型变量hilarious，将False值赋给hilarious
joke_evaluation = "Isn't that joke so funny?! %r"    #把字符串赋值给joke_evaluation变量

print joke_evaluation % hilarious                    #把调用hilarious变量的joke_evaluation变量打印出来

w = "This is the left side of..."
e = "a string with a right side."

print w + e                                          #将w和e变量的字符串加在一起显示
