# 2D lists = a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food[0])

print(food[0][0])

for i in range(len(food)):
    for j in range(len(food[i])):
        print(food[i][j] + " ", end="")
    print()
