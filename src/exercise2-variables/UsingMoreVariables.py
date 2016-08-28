my_name = "Harsh Rastogi"
first_name_initial = 'H'
last_name_initial = 'R'
my_age = 23
my_height = 175  # cms
my_weight = 62  # kgs
my_eyes = "brown"
my_teeth = "yellow"
my_hair = "black"

# %s is one of the format specifiers which is used to modify a string.
# %d or %i - decimal, integer
# %o -  octal
# %x, %X - unsigned hexadecimal, lower case and upper case
# %e, %E - floating point exponential format, lower case and upper case
# %f, %F - floating point decimal
# %c - single character also accepts integer

# %s, %d and %c
print "Let's talk about %s ." % my_name
print "His first name initial is %c." % first_name_initial
print "His last name initial is %c." % last_name_initial
print "He is %d centimeters tall." % my_height
print "He is %d kilograms heavy." % my_weight
print "Working on gaining weight."
print "He has got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are always %s whatever happens." % my_teeth
print "If I add %i, %d, %d then I get %d." % (my_age, my_height, my_weight, (my_age + my_height + my_weight))

# %f, %F
ratio_height_age = my_height / my_age
print "Ratio of his height and age is %f." % ratio_height_age

# The length of the appended value can be modified by specifying
#  the length before the specifier character, in case of
# culling the numbers after decimal point using decimal point before the length.
print "The ratio with three decimal after point is %.3F." % ratio_height_age

# %o, %x and %X I guess you are aware of octal and hexadecimal numbers
decimal_value = 256
decimal_value1 = 13989321323
print "The octal value of %d is %o" % (decimal_value, decimal_value)
print "The hexadecimal value of %d is %x" % (decimal_value1, decimal_value1)  # lower case
print "The hexadecimal value of %d is %X" % (decimal_value1, decimal_value1)  # upper case
print "The exponential equivalent of %d is %e." % (decimal_value1, decimal_value1)
