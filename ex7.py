# coding: utf-8
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'  #这里注意的是要写成'snow'，而不能直接写snow。少了单引号就相当于调用snow这个变量，而在程序中并没有定义snow
print "And everywhere that Mary went."
print "."  * 10  # what'd that do?  Its function is showing '.' by multipling 10 times.
print "SB" * 10

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12    #print语句的逗号在输出显示给用户看时，相当于空格效果。如果不加逗号，则会分行显示
