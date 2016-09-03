# this is like the argv we have been using
# it can accept as many arguments as you want


#  Writing the body of a function is also called defining a function
# here def stands for define
# followed by function name which defines what the function does
# followed by a pair of parenthesis
# followed by a colon
# in the next line we right the code for function
def print_two(*argv):
    arg1, arg2 = argv
    print "function : print_two\narg1: %r, arg2: %r" % (arg1, arg2)


# method with exact two parameters
def print_two_2(arg1, arg2):
    print "function : print_two_2 \narg1: %r, arg2: %r" % (arg1, arg2)


# method/function with exact one parameter
def print_one(arg):
    print "function : print_one \narg : %r" % arg


# function with no parameter
def print_none():
    print "I got nothing."


# calling functions with arguments
print_two("Harsh", "Rastogi")
print_two_2('Harsh', 'Rastogi')
print_one("Meerut")
print_none()

# run
# $ python BasicFunctions.py
# output
# function : print_two
# arg1: 'Harsh', arg2: 'Rastogi'
# function : print_two_2
# arg1: 'Harsh', arg2: 'Rastogi'
# function : print_one
# arg : 'Meerut'
# I got nothing.
