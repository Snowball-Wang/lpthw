# -*- coding: GBK -*-
import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

## 创建一个PHRASES的dict
PHRASES = {
    "class %%%(%%%):":
     "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
     "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self,@@@)":
     "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
     "Set *** to an instance of class %%%.",
    "***.***(@@@)":
     "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
     "From *** get the *** attribute and set it to '***'."
    }

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":   ## 判断python命令行输入的参数的个数是否为2，且第二个参数是否为"english"
    PHRASE_FIRST = True                               ## 若是，则将变量PHRASE_FIRST设置为True
else:
    PHRASE_FIRST = False                              ## 若不是，则将变量PHRASE_FIRST设置为False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():            ## 通过urlopen模块打开对应链接，并读取网页内容（其实就是简单的爬取网页信息）
    WORDS.append(word.strip())                        ## .strip()函数把对应字符串的前后空格去掉，留下中间字符串，且字符串中间可包含空格


def convert(snippet,phrase):                            
    class_names = [w.capitalize() for w in                          ## random.sample()在WORDS序列获取snippet.count(...)长度的片段，
                   random.sample(WORDS,snippet.count("%%%"))]       ## 并将每个元素的首字母大写   
    other_names = random.sample(WORDS,snippet.count("***"))         ## 原理同上
    results = []                                                    ## 创建一个名为results的空列表
    param_names = []                                                ## 创建一个名为param_names的空列表

    if snippet.count("@@@") > 0:
        param_count = random.randint(1,3)                                 ## 设置参数的个数为1-3中三个数的随机一个数
        param_names.append(', '.join(random.sample(WORDS, param_count)))  ## 通过.join()函数把随机数目的参数连接起来

    for sentence in snippet, phrase:
        result = sentence[:]            #这条语句的作用是把snippet列表的内容和phrase列表的内容分别遍历一遍，先是snippet遍历，再是phrase遍历

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)          ## 用word取代原字符串中的%%%符号，并且限制最大的取代次数为1

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)          ## 同理，用word取代原字符串中的***符号，也限制最大的取代次数为1

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)          ## 同上

        results.append(result)                               ## 就相当于把替换过后的字符串赋值给results这个空的列表list

    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()                      ## 将字典PHRASES里的key值赋值给变量snippets，snippets是一个列表
        ##print snippets  测试使用
        random.shuffle(snippets)                       ## random.shuffle()函数将snippets列表里的元素随机打乱

        for snippet in snippets:
            phrase = PHRASES[snippet]                  ## 将PHRASES字典里的value值赋值给变量phrase
            question, answer = convert(snippet, phrase)## 调用convert()函数，并将返回值分别赋值给question, answer两个变量
            if PHRASE_FIRST:
                question, answer = answer, question    ## 如果参数是两个，且第二个参数是english，则将question和answer两个变量换过来

            print question

            if PHRASE_FIRST:
                raw_input("> ")                            ## 这里面有一个bug，就是在给你代码含义让你写代码时，如果要写的代码时两行，但实际上
                raw_input("> ")                            ## 你只能写一行
            else:
                raw_input("> ")
            print "ANSWER: %s\n\n" % answer                

except EOFError:   ## Raised when one of the built-in functions  
    print "\nBye"  ## (input() or raw_input()) hits an end-of-file condition (EOF) without reading any data.
