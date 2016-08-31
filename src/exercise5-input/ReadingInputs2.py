# using raw_input(message) you can also show a prompt message

seconds = raw_input("How many seconds are there in a minute?")
minutes = raw_input("How many minutes are there in an hour?")
hours = raw_input("How many hours are there in a day?")

print "There are %s hours in a day, " % hours,
print "%s minutes in an hour " % minutes,
print "and %s seconds in a minute.\n" % seconds

# what if we want to use the inputs as numbers
# int() is used to convert the string value to an integer
hours_in_a_day = int(raw_input("Enter hours in a day "))

print "There are %d minutes in a day." % (hours_in_a_day * 60)
print "There are %d seconds in a day." % (hours_in_a_day * 60 * 60)
