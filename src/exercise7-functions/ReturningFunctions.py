def add(a, b):
    print "ADDING %d + %d." % (a, b)
    return a + b


def subtract(a, b):
    print "SUBTRACTING %d - %d." % (a, b)
    return a - b


def multiply(a, b):
    print "MULTIPLYING %d * %d." % (a, b)
    return a * b


def divide(a, b):
    print "DIVIDING %d / %d." % (a, b)
    return a / b


print "Let's do some math with functions."

age = add(50, 10)
height = multiply(30, 2)
weight = divide(80, 2)
iq = subtract(45, 32)

print "Age: %d, height %d, weight %d, IQ %d" % (age, height, weight, iq)

# nested function calls
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes ", what

