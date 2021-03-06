# coding: utf-8
import ex25
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
#def print_first_word(words)  错误1，函数定义后没有加冒号
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	#word = words.poop(0)  错误2，pop拼写有误
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	#word = words.pop(-1  错误3，少了个右括号
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
#five = 10 - 2 + 3 - 5	 错误4，计算错误
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	#jars = jelly_beans \ 1000	错误5，除法的斜杠是左斜杠
	crates = jars / 100
	return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)
#beans, jars, crates == secret_formula(start-point) 错误6,7 这条语句是赋值语句,
#所以用的应该是=号，上条语句的参数是start_point，所以括号里的参数必须是start_point

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)
#print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont   错误8，参数的写法有问题


sentence = "All god\tthings come to those who weight."

words = ex25.break_words(sentence)	  #错误9，没有import ex25这个模块
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
#.print_first_word(sorted_words)   错误10，程序语句多了个.
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)	  #错误11，没有导入ex25这个模块
print sorted_words		#错误12，print写的不完整
#prin sorted_words

print_first_and_last(sentence)
#print_irst_and_last(sentence)	错误13，函数名拼写有错误  

print_first_and_last_sorted(sentence)
   #print_first_a_last_sorted(senence)	错误14,15,16 首行不用缩进，函数名拼写有错误，参数名拼写有错误
