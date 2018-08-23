# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse",24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage",15.45]

print(areas)
print(areas_1)
print(areas_2)

######List Comprehension#########
#If you used to do it like this:
new_list = []
for i in old_list:
    if filter(i):
        new_list.append(expressions(i))
#You can obtain the same thing using list comprehension:
new_list = [expression(i) for i in old_list if filter(i)]
