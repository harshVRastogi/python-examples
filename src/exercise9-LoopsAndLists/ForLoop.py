the_count = [1, 2, 3, 4, 5]
fruits = ["mango", 'apple', "pineapple", "orange", "papaya", 'guava']
change = [1, 'rupee', 2, "ruppes", 3, "paisa"]

for count in the_count:
    print "This is count %d" % count

for fruit in fruits:
    print "This is %s fruit" % fruit

for i in change:
    print "This is change %r" % i

elements = []

for i in range(0, 6):
    elements.append(i)

for e in elements:
    print "This is element %d" % e

# run
# $ python ForLoop.py
# output
# This is count 1
# This is count 2
# This is count 3
# This is count 4
# This is count 5
# This is mango fruit
# This is apple fruit
# This is pineapple fruit
# This is orange fruit
# This is papaya fruit
# This is guava fruit
# This is change 1
# This is change 'rupee'
# This is change 2
# This is change 'ruppes'
# This is change 3
# This is change 'paisa'
# This is element 0
# This is element 1
# This is element 2
# This is element 3
# This is element 4
# This is element 5
