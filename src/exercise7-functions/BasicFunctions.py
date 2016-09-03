# this is like the argv we have been using
# it can accept as many arguments as you want


#  Writing the body of a function is also called defining a function
def print_two(*argv):
    arg1, arg2 = argv
    print "function : print_two\n arg1: %r, arg2: %r" % (arg1, arg2)


# method with exact two parameters
def print_two_2(arg1, arg2):
    print "function : print_two_2 \n arg1: %r, arg2: %r" % (arg1, arg2)


# method/function with exact one parameter
def print_one(arg):
    print "function : print_one \n arg : %r" % arg


# function with no parameter
def print_none():
    print "I got nothing."


# calling functions with arguments
print_two("Harsh", "Rastogi")
print_two_2('Harsh', 'Rastogi')
print_one("Meerut")
print_none()
