# Variable is used to save the result of a calculation or assigning a number.

# Number of cars to be 100
cars = 100
# There is space for 4 people in a car
space_in_car = 4.0
# Available drivers
drivers = 30
# total passengers
passengers = 90
# total cars that could not be driven because of the lack of drivers
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

print "There are ", cars, " cars available."
print "There are only ", drivers, " drivers available."
print "There will be ", cars_not_driven, " empty cars today."
print "We can transport ", carpool_capacity, " people today."
print "We have ", passengers, " passengers to carpool today."
print "We need to put about", average_passengers_per_car, " passengers per car."
