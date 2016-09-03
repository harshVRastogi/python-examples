def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses." % cheese_count
    print "You have %d boxes of crackers\n" % boxes_of_crackers


print "We can just give the function numbers directly."
cheese_and_crackers(20, 50)

print "Or we can use variables from our script."
number_of_cheeses = 30
number_of_cracker_boxes = 50

cheese_and_crackers(number_of_cheeses, number_of_cracker_boxes)

print "We can even do math inside."
cheese_and_crackers(45 + 23, 50 - 10)

print "We can combine the two variables inside."
cheese_and_crackers(number_of_cheeses + 23, number_of_cracker_boxes - 20)

# run
# $ python BasicFunctions.py
# output
# We can just give the function numbers directly.
# You have 20 cheeses.
# You have 50 boxes of crackers
#
# Or we can use variables from our script.
# You have 30 cheeses.
# You have 50 boxes of crackers
#
# We can even do math inside.
# You have 68 cheeses.
# You have 40 boxes of crackers
#
# We can combine the two variables inside.
# You have 53 cheeses.
# You have 30 boxes of crackers
