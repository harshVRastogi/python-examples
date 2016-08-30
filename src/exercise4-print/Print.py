formatter = "%r %r %r %r"
print formatter % (2, 3, 4, 5)
print formatter % ("two", "three", "four", "five")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "She's got that style",
    "She's got that smile " + "She's got that xing",
    "That one thing ",
    "She's got a ####")
