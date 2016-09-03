from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s." % (from_file, to_file)

# in_file = open(from_file) old way
in_data = open(from_file).read()

print "The input file is %d bytes long." % len(in_data)

print "Does the output file exists? %r?" % exists(to_file)
print "Hit enter to continue, ctrl + c to exit."

raw_input()

# out_file = open(to_file, 'w')
open(to_file, 'w').write(in_data)

print "Copying done!"

# in_file.close()
# out_file.close()
# no need to close file when with the reading the new way

