from nose.tools import *
from ex49 import lexicon
from ex49 import parser

def test_sentence_obj():
    s = parser.Sentence(('noun', 'princess'),('verb', 'eat'),('number', 1),('noun', 'bear'))
    assert_equal(s.subject, 'princess')
    assert_equal(s.verb, 'eat')
    assert_equal(s.number, 1)
    assert_equal(s.object, 'bear')

def test_peek():
    word_list = lexicon.scan('princess eat 1 bear')
    assert_equal(parser.peek(word_list), 'noun')
    assert_equal(parser.peek(None),None)

def test_match():
    word_list = lexicon.scan('princess eat 1 bear')
    assert_equal(parser.match(word_list,'noun'),('noun','princess'))
    assert_equal(parser.match(word_list,'verb'),('verb','eat'))
    assert_equal(parser.match(word_list,'number'),('number',1))
    assert_equal(parser.match(word_list,'stop'),None)
    assert_equal(parser.match(None,'noun'),None)

def test_skip():
    word_list = lexicon.scan('princess eat 1 bear')
    parser.skip(word_list,'noun')
    assert_equal(word_list,[('verb','eat'),('number',1),('noun','bear')])
    parser.skip(word_list,'verb')
    assert_equal(word_list,[('number',1),('noun','bear')])
    parser.skip(word_list,'number')
    assert_equal(word_list,[('noun','bear')])
    parser.skip(word_list,'noun')
    assert_equal(word_list,[])

def test_parse_verb():
    word_list = lexicon.scan('it eat 1 bear')
    assert_equal(parser.parse_verb(word_list),('verb','eat'))
    word_list = lexicon.scan('the kill princess')
    assert_equal(parser.parse_verb(word_list),('verb','kill'))
    word_list = lexicon.scan('princess eat 1 bear')
    assert_raises(parser.ParserError, parser.parse_verb, word_list)

def test_parse_object():
    word_list = lexicon.scan('it bear')
    assert_equal(parser.parse_object(word_list),('noun','bear'))
    word_list = lexicon.scan('the south')
    assert_equal(parser.parse_object(word_list),('direction','south'))
    word_list = lexicon.scan('princess eat 1 bear')
    assert_equal(parser.parse_object(word_list),('noun','princess'))
    word_list = lexicon.scan('it kill')
    assert_raises(parser.ParserError, parser.parse_object, word_list)

def test_parse_subject():
    word_list = lexicon.scan('eat bear')
    subj = ('noun','princess')
    num = ('number',1)
    s = parser.parse_subject(word_list,subj,num)
    assert_equal((s.subject,s.verb,s.number,s.object), ('princess','eat',1,'bear'))

def test_parse_sentence():
    word_list = lexicon.scan('princess eat bear')
    s = parser.parse_sentence(word_list)
    assert_equal((s.subject,s.verb,s.number,s.object),('princess','eat',1,'bear'))
    word_list = lexicon.scan('kill princess')
    s = parser.parse_sentence(word_list)
    assert_equal((s.subject,s.verb,s.number,s.object),('player','kill',1,'princess'))
    word_list = lexicon.scan('north kill princess')
    assert_raises(parser.ParserError, parser.parse_sentence,word_list)

