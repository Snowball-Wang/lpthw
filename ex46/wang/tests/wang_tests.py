from nose.tools import *
from wang import *

def setup():
	print "SETUP!"

def teardown():
	print "TEAR DOWN!"

def test_basic():
	print "I RAN!"

def haha():
	weather.showWeather("suuny")
	
