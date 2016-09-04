from sys import argv


def print_all(f):
    print f.read()


# make the pointer of file return back to the start of file which first byte in the file
def rewind_file(f):
    f.seek(0)


def print_line(f, line_count):
    print line_count, f.readline()


script, filename = argv

my_file = open(filename)

print "First print the whole file."
print_all(my_file)

print "Let's rewind the file like a tape."
rewind_file(my_file)

current_line = 1

print "Now print line by line."

print "Line 1"
print_line(my_file, current_line)

# += is a shorthand operator
#  which shortens the operation variable1 = variable1 + constant/variable2
# to variable1 += constant/variable2
# you can use it with other operator also
#  variable1 -= constant/variable2
#  variable1 *= constant/variable2
#  variable1 /= constant/variable2

current_line += 1

print "Line 2"
print_line(my_file, current_line)

current_line += 1

print "Line 3"
print_line(my_file, current_line)

my_file.close()

# run
# $ python FunctionAndFiles.py textfile.txt
# First print the whole file.
# This is line 1.
# This is line 2.
# This is line 3.
# Let's rewind the file like a tape.
# Now print line by line.
# Line 1
# 1 This is line 1.
#
# Line 2
# 2 This is line 2.
#
# Line 3
# 3 This is line 3.

