import random

gestures = ['rock', 'scissors', 'paper']
win_combination = [['rock','scissors'],['scissors','paper'],['paper', 'rock']]

while True:
        computer = random.choice(gestures)
	people = raw_input('Please input:'.strip())
	if people not in gestures:
	    continue
	elif computer == people:
	    print 'Draw'
	elif [computer, people] in win_combination:
	    print 'Computer wins!'
	else:
	    print 'People wins!'
    

