# tuple =   collection which is ordered and unchangeable
#                used to group together related data

student = ("HK", 18, "Computer Science")

print(student.count("HK"))
print(student.index("Computer Science"))

for x in student:
    print(x)

if "HK" in student:
    print("HK is here!")
