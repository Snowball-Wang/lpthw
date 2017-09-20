# -*- coding: GBK -*-
import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

## ����һ��PHRASES��dict
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
if len(sys.argv) == 2 and sys.argv[1] == "english":   ## �ж�python����������Ĳ����ĸ����Ƿ�Ϊ2���ҵڶ��������Ƿ�Ϊ"english"
    PHRASE_FIRST = True                               ## ���ǣ��򽫱���PHRASE_FIRST����ΪTrue
else:
    PHRASE_FIRST = False                              ## �����ǣ��򽫱���PHRASE_FIRST����ΪFalse

# load up the words from the website
for word in urlopen(WORD_URL).readlines():            ## ͨ��urlopenģ��򿪶�Ӧ���ӣ�����ȡ��ҳ���ݣ���ʵ���Ǽ򵥵���ȡ��ҳ��Ϣ��
    WORDS.append(word.strip())                        ## .strip()�����Ѷ�Ӧ�ַ�����ǰ��ո�ȥ���������м��ַ��������ַ����м�ɰ����ո�


def convert(snippet,phrase):                            
    class_names = [w.capitalize() for w in                          ## random.sample()��WORDS���л�ȡsnippet.count(...)���ȵ�Ƭ�Σ�
                   random.sample(WORDS,snippet.count("%%%"))]       ## ����ÿ��Ԫ�ص�����ĸ��д   
    other_names = random.sample(WORDS,snippet.count("***"))         ## ԭ��ͬ��
    results = []                                                    ## ����һ����Ϊresults�Ŀ��б�
    param_names = []                                                ## ����һ����Ϊparam_names�Ŀ��б�

    if snippet.count("@@@") > 0:
        param_count = random.randint(1,3)                                 ## ���ò����ĸ���Ϊ1-3�������������һ����
        param_names.append(', '.join(random.sample(WORDS, param_count)))  ## ͨ��.join()�����������Ŀ�Ĳ�����������

    for sentence in snippet, phrase:
        result = sentence[:]            #�������������ǰ�snippet�б�����ݺ�phrase�б�����ݷֱ����һ�飬����snippet����������phrase����

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)          ## ��wordȡ��ԭ�ַ����е�%%%���ţ�������������ȡ������Ϊ1

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)          ## ͬ����wordȡ��ԭ�ַ����е�***���ţ�Ҳ��������ȡ������Ϊ1

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)          ## ͬ��

        results.append(result)                               ## ���൱�ڰ��滻������ַ�����ֵ��results����յ��б�list

    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()                      ## ���ֵ�PHRASES���keyֵ��ֵ������snippets��snippets��һ���б�
        ##print snippets  ����ʹ��
        random.shuffle(snippets)                       ## random.shuffle()������snippets�б����Ԫ���������

        for snippet in snippets:
            phrase = PHRASES[snippet]                  ## ��PHRASES�ֵ����valueֵ��ֵ������phrase
            question, answer = convert(snippet, phrase)## ����convert()��������������ֵ�ֱ�ֵ��question, answer��������
            if PHRASE_FIRST:
                question, answer = answer, question    ## ����������������ҵڶ���������english����question��answer��������������

            print question

            if PHRASE_FIRST:
                raw_input("> ")                            ## ��������һ��bug�������ڸ�����뺬������д����ʱ�����Ҫд�Ĵ���ʱ���У���ʵ����
                raw_input("> ")                            ## ��ֻ��дһ��
            else:
                raw_input("> ")
            print "ANSWER: %s\n\n" % answer                

except EOFError:   ## Raised when one of the built-in functions  
    print "\nBye"  ## (input() or raw_input()) hits an end-of-file condition (EOF) without reading any data.
