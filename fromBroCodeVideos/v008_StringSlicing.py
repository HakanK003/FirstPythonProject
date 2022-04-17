# can be used for different collections

# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Iron Man"

first_name = name[:4]  # [0:4]
last_name = name[5:]  # [5:end]
funky_name = name[::2]  # [0:end:2]
reversed_name = name[::-1]  # [0:end:-1]

print(reversed_name)

#############################################################

first_name2 = name[:name.find(" ")]
last_name2 = name[name.find(" ")+1:]

print(first_name2)
print(last_name2)

#############################################################

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)  # negative indexes start from -1

print(website1[slice])
print(website2[slice])
