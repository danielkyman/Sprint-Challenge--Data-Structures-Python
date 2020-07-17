import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#############


def binarySearch(values, value):
    if len(values) == 1:
        if values[0] is value:
            return True
        else:
            return False
    elif value == values[int(len(values)/2)]:
        return True
    elif value < values[int(len(values)/2)]:
        newValues = values[0:int(len(values)/2)]
        return binarySearch(newValues, value)
    else:
        newValues = values[int(len(values)/2):]
        return binarySearch(newValues, value)


names_1.sort()

for name in names_2:
    if binarySearch(names_1, name):
        duplicates.append(name)
#############


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
