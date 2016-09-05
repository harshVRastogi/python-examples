class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


love = Song(["You'r beautiful, Its true",
             "I saw your face in a crowded place",
             "And I don't know what to do",
             "Cause I've never be with you"])

bulls_of_parade = Song(["They rally around the family",
                        "With pocket full of shells"])

love.sing_me_a_song()
bulls_of_parade.sing_me_a_song()

# run
# $ python Song.py
# output
# You'r beautiful, Its true
# I saw your face in a crowded place
# And I don't know what to do
# Cause I've never be with you
# They rally around the family
# With pocket full of shells
