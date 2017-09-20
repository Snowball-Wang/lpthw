class Song(object):
    
	def __init__(self,lyrics,author):
	    self.lyrics = lyrics
	    self.author = author
	
	def sing_me_a_song(self):
	    for line in self.lyrics:
                    print line
                    
        def show_me_the_author(self):
                for line in self.author:
                        print line
	
	
			
happy_bday = Song(["Happy birthday to you","I don't want to get sued", "So I'll stop right here"],["various artist","pop music"])


bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"],["various artist","folk music"])

happy_bday.sing_me_a_song()

happy_bday.show_me_the_author()

print '-' * 10

bulls_on_parade.sing_me_a_song()

bulls_on_parade.show_me_the_author()

print '-' * 10

yellow = Song(["Look at the star", "Look how they shine for you", "All the things you do","Oh, they are all yellow"],["coldplay","rock music"])

yellow.sing_me_a_song()

yellow.show_me_the_author()
