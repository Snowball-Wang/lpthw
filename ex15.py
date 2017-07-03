# coding: utf-8
from sys import argv  #导入argv模块

script, filename = argv  #两个变量script, filename。把argv中的东西解包，将所有的参数依次赋值给左边的这些变量。

txt = open(filename)      #open指令返回的是一个file object.此语句的作用相当于把test.txt文件拷贝给txt

print "Here's your file %r:"  % filename
print txt.read()          #读取txt文件的内容
print txt.close()         #关闭txt文件

#print "Type the filename again:"
#file_again = raw_input("> ")  

#txt_again = open(file_again)  #将test.txt文件再次拷贝给txt_again

#print txt_again.read()        #再次打开test.txt文件
