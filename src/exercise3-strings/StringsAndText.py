# formatting string before assigning to the variable x
x = "There are %d types of people in the world." % 10

# two string literals
binary = "binary"
do_not = "don't"

# using the variables to format the string
y = "Those who understand %s and those who %s." % (binary, do_not)

# print x and y
print x
print y

# %r is used for raw data so it contains single quotes as it was not
#  formatted to show the output to users but to debug the operation
# single quotes used to show the value of y in single quotes
print "I said: %r." % x
print "I also said: '%s'." % y

# showing value of variable x in double quotes
print 'I said: "%s".' % x

# \" is used to print the double quotes with syntax error if double quotes are used for the main string
print "I also said: \"%s\"." % y

hilarious = False
joke_evaluation = "Isn't this joke so funny? %r"

# we print the string variable with a format specifier %r then print the value for the specifier with a % in between
print joke_evaluation % hilarious

w = "This is the left side of a String..."
z = "And this is the right side."

# the plus sign is used to concatenate two strings.
# + sign has other effects also if used with strings and numbers at the same time.
print w + z

