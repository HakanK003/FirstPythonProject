# set = collection which is unordered, un-indexed. No duplicate values. Faster than lists

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)  --> add utensils to dishes  --> adding new elements
# dinner_table = utensils.union(dishes)  --> merges utensils to dishes

# print(dishes.difference(utensils))  --> returns uncommon elements
# print(utensils.intersection(dishes))  --> returns common elements

for x in utensils:
    print(x)
