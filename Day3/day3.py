
with open("input.txt") as f:
    data = f.readlines()

items = [i for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
priorities = [p for p in range(1,53)]
itemPriorities = dict(zip(items, priorities))

sharedItems = []
for line in data:
    compartmentLength = (len(line) - 1) // 2
    compartment1 = line[0:compartmentLength]
    compartment2 = line[compartmentLength:]

    for item in compartment1:
        if item in compartment2:
            sharedItems.append(item)
            break

sum_of_priorities = 0
for item in sharedItems:
    sum_of_priorities += itemPriorities[item]

print(sum_of_priorities)
