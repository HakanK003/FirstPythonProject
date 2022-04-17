from v038_ClassVariables_Car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

# Car.wheels = 2 if you change like this it will affect all the cars
# car_1.wheels = 2 if you change like this it will affect only car_1

print(car_1.wheels)
print(car_2.wheels)
