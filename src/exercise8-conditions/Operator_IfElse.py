print "You enter a dark room with two doors. Do you go through door #1 or door #2?"
door = raw_input('>')
if door == "1":
    print "There is a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at bear."

    bear = raw_input('>')

    if bear == "1":
        print "Bear eats your face off. Good job!"
    elif bear == 2:
        print "Bear eats your tounge with cake cream."
    else:
        print "Well doing %s is better. Bear runs away!" % bear

elif door == "2":
    print "You stare at endless abyss at cthulu's retina."
    print "1. Blue berries."
    print "Yellow jacket clothespins."
    print "Understanding revolvers yelling melodies."

    insanity = raw_input('>')

    if insanity == '1' or insanity == '2':
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
else:
    print "You stumble around, fall on a knife and die. Good job!"

# run
# python operator_IfElse.py
# output
# You enter a dark room with two doors. Do you go through door #1 or door #2?
# >1
# There is a giant bear here eating a cheese cake. What do you do?
# 1. Take the cake.
# 2. Scream at bear.
# >1
# Bear eats your face off. Good job!
