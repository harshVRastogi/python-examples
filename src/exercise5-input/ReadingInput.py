# raw_input() is a method to make you enter a value in console
# and read it.
# so basically raw_input takes the value from console and treat it as a string
# comma is used after the print statement to keep the input in the same
# line otherwise python would print it in the new line
print "How old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weigh?",
weight = raw_input()

print "So you are %r year old, weigh %r and %r centimeters tall." % (age, height, weight)

# play with it more

print "What was your School name?",
school_name = raw_input()

print "How many student were there in total?",
number_of_students = raw_input()

print "How many teachers were there?",
number_of_teachers = raw_input()

print """Your school name was %r.\nThere were %r students and %r teachers.""" % (
    school_name, number_of_students, number_of_teachers)
