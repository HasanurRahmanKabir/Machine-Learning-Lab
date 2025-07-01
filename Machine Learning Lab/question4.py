# Write a program to find all unique elements in the list.

my_list = [12, 11, 22, 34, 54, 33, 12, 11, 34, 98, 34, 34, 35, 78]
unique = []

for item in my_list:
    if my_list.count(item) == 1:
        unique.append(item)

print(unique)
