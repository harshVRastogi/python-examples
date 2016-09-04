ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait! There is not ten thing in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_item = more_stuff.pop()
    print "Adding :", next_item
    stuff.append(next_item)
    print "There is %d items now." % len(stuff)

print "There we go."
print stuff

print "Let's do somethings with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
