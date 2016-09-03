from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want that hit Ctrl+c."
print "If you do hit enter."

# raw_input for user's confirmation to erase the file
raw_input()


print "Opening the file..."
target_file = open(filename, 'w')

print "Truncating the file contents."
target_file.truncate()

print "Enter three lines"

line1 = raw_input("Line 1:>")
line2 = raw_input("Line 2:>")
line3 = raw_input("Line 3:>")

print "Writing to your file"

target_file.write(line1)
target_file.write('\n')

target_file.write(line2)
target_file.write('\n')

target_file.write(line3)
target_file.write('\n')

target_file.close()
print "File closed."
