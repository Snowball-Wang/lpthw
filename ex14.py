from sys import argv

script, user_name, user_degree = argv
prompt = '### '

print "Hi %s of %s degree, I'm the %s script." % (user_name, user_degree, script)
print "I'd like to ask you a few question."
print "Do you like me %s?" % user_name 
likes = raw_input (prompt)

print "Where do you live %s?" % user_name
lives = raw_input (prompt)

print "What kind of computer do you have?"
computer = raw_input (prompt)

print """
Alright, so you said %r about liking me.
you live in %r. Not sure where that is.
And you have a %r computer. Nice.
"""  % (likes, lives, computer)
