def draw_border(num):
    print '-' * num


# create a mapping between names and abbreviation
states = {
    'Uttar Pradesh': 'UP',
    'Uttrakhand': 'UK',
    'Madhaya Pradesh': 'MP',
    'Jammu and Kashmir': 'J&K',
    'Karnataka': 'KN',
    'Maharashtra': 'MH',
    'Punjab': 'PB'}

# create a mapping between state abbreviation and city name
cities = {
    'UP': 'Meerut',
    'UK': 'Karna Prayag',
    'KN': 'Bangaluru',
    'MH': 'Mumbai',
    'PB': 'Chandigrah'}

# added some more cities in states
cities['J&K'] = 'Kashmir'
cities['MP'] = 'Bhopal'

# print city names with key used in mapping
draw_border(20)
print "UP state has : ", cities['UP']
print "UK state has : ", cities['UK']

# print state abbreviation with key used in mapping
draw_border(20)
print "Uttar Pradesh's abbreviation is : ", states['Uttar Pradesh']
print "Maharashtra's abbreviation is : ", states['Maharashtra']

# print city names with the use of state names
draw_border(20)
print "Uttar Pradesh has", cities[states['Uttar Pradesh']]
print "Uttrakhand has", cities[states['Uttrakhand']]

# print the state name and its abbreviation
draw_border(20)
for state, abbr in states.items():
    print "%s is abbreviated as %s" % (state, abbr)

# print the state abbreviation and its city
draw_border(20)
for abbr, city in cities.items():
    print "%s has the city %s" % (abbr, city)

# print above two prints combined in one
draw_border(20)
for state, abbr in states.items():
    print "%s is abbreviated %s and has city %s" % (abbr, state, cities[abbr])

# printing with a check
draw_border(20)
states = states.get('Delhi')
if not state:
    print "Sorry, no Delhi."

# printing with default value
city = cities.get("DL", "Does not exists.")
print "The city for the state DL is : %s" % city


# run
# $ python Dictionary.py
# output
# --------------------
# UP state has :  Meerut
# UK state has :  Karna Prayag
# --------------------
# Uttar Pradesh's abbreviation is :  UP
# Maharashtra's abbreviation is :  MH
# --------------------
# Uttar Pradesh has Meerut
# Uttrakhand has Karna Prayag
# --------------------
# Jammu and Kashmir is abbreviated as J&K
# Madhaya Pradesh is abbreviated as MP
# Punjab is abbreviated as PB
# Uttrakhand is abbreviated as UK
# Maharashtra is abbreviated as MH
# Uttar Pradesh is abbreviated as UP
# Karnataka is abbreviated as KN
# --------------------
# J&K has the city Kashmir
# KN has the city Bangaluru
# MH has the city Mumbai
# UP has the city Meerut
# PB has the city Chandigrah
# MP has the city Bhopal
# UK has the city Karna Prayag
# --------------------
# J&K is abbreviated Jammu and Kashmir and has city Kashmir
# MP is abbreviated Madhaya Pradesh and has city Bhopal
# PB is abbreviated Punjab and has city Chandigrah
# UK is abbreviated Uttrakhand and has city Karna Prayag
# MH is abbreviated Maharashtra and has city Mumbai
# UP is abbreviated Uttar Pradesh and has city Meerut
# KN is abbreviated Karnataka and has city Bangaluru
# --------------------
# The city for the state DL is : Does not exists.
