# cars gets value 100
cars = 100
# space_in_a_car = 4.0
# spaces gets value 4
space_in_a_car = 4 # changing to 4 prints carpool_capacity as an integer
# drivers gets value 30
drivers = 30
# passengers gets value 90 
passengers = 90
# cars_not_driven gets value of 70
cars_not_driven = cars - drivers
# cars_driven gets value 30
cars_driven = drivers
# carpool_capacity gets value 120
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car gets floating point value 3.0
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
