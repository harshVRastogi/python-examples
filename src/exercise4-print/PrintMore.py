days = "Sun Mon Tue Wed Thurs Fri Sat"
# \n is used to add new line in a string and is one of the escape sequences
# \n doesn't work with %r as it shows the string as you put it
months = "January\nFebruary\nMarch\nApril\nMay\nJune\nJuly\nAugust\nSeptember\nOctober\nNovember\nDecember"

print "Here are the days: %s" % days
print "Here are the months : %s" % months
print "Here are the months : %r" % months

# using double quotes three time to make a multi line string
# don't put spaces between double quotes.
# (" " ") don't do this
print """
There's something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want or 5 or 6.
"""
