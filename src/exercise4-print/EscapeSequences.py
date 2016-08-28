# escape sequences are used to put difficult-to-type characters into a string

# print "I am 6'2" tall" wii give you a syntax error
# as the double quotes for inches you used would be interpreted as string closing
# the right way is to put a backslash before double quote

print "I am 5'10\" tall."

# similarly for single quote
print 'I am 5\'10" tall.'

# or used triple quotes
# the end is considered only when the closing  triple quotes are found
print """I am 5'10" tall."""

# \\ Backslash (\)
# \' Single quote (')
# \" Double quote (")
# \a ASCII bell read more about bell character https://en.wikipedia.org/wiki/Bell_character
# \b ASCII backspace
# \f ASCII form feed
# \n new line
# \r ASCII carriage return
# \t ASCII horizontal tab
# \uxxxx Character with 16 bit hex value (unicode only)
# \Uxxxxxxxx Character with 32 bit hex value (unicode only)
# \v ASCII vertical tab
# \0oo character with octal value oo
# \xhh character with hex value hh

tabby_cat = "\tI am tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\a\\ cat."
fat_cat = '''
I'll do a list:
\t*\acat food
\t*\afishies
\t*\acatnip \n\t*\agrass
'''

my_name = "Harsh \r Rastogi"

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print my_name
# Unicode value of a is 0041 which is in hex
print u"\u0041"
print u"\u00B0\u0048\u0041\u0052\u0053\u0048\u00B0"
print "\077"  # can't go beyond 77 as it's octal
print "\x48\x41\x52\x53\x48"
