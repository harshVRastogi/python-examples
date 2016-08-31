from sys import argv

script, filename = argv

# method open() is used to open a file
txt = open(filename)

# txt becomes a file  when you open a file and assigns it to variable txt
# read() is a method of file which reads its contents
# txt.read() tells the txt file to read its contents
print "Your file name is %r." % filename
print "Content of your file:\n%s" % txt.read()

print "Type the file name again :"

filename2 = raw_input(">")
txt2 = open(filename2)

# txt2.read() gives the contents of a file which print method can print directly
print txt2.read()
