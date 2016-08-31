from sys import argv

script, x, y, z = argv

print "X : ", x
print "Y : ", y
print "Z : ", z

hours_in_day = int(raw_input("Enter hours in day:"))
days_in_month = int(raw_input("Enter days in a month:"))
months_in_year = int(raw_input("Enter months in a year:"))

count = 1
print "\n%d:In a year there are :" % count
print "%d hours" % (hours_in_day * days_in_month * months_in_year)
print "%d minutes" % (60 * hours_in_day * days_in_month * months_in_year)

# wouldn't it be better to save calculation in a variable to reuse
hours_in_year = hours_in_day * days_in_month * months_in_year
count = count + 1

#

print "\n%d:In a year there are :" % count
print "%d hours" % hours_in_year
print "%d minutes" % (60 * hours_in_year)
# calculate for seconds and milliseconds
