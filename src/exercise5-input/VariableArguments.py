# using import you include the feature you specify after import keyword
# every language has a vast pool of features or libraries or modules
# which are imported when the user requires to keep the program as small as possible
from sys import argv

# here python unpacks the variables you entered in the console
# enter exact number of variables you have declared with argv
script, first, second, third = argv
# argv stand for argument variable

# arguments are the values you pass to a module
print "The script name is:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# to run the script type
# python VariableArguments.py first_variable second_variable third_variable
# the value of the variables would be anything


