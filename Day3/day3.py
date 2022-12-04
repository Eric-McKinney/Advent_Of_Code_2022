
with open("input.txt") as f:
    data = f.readlines()

items = [i for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
priorities = [p for p in range(1,53)]
item_priorities = dict(zip(items, priorities))

shared_items = []
for line in data:
    compartment_length = (len(line) - 1) // 2
    compartment_1 = line[:compartment_length]
    compartment_2 = line[compartment_length:]

    for item in compartment_1:
        if item in compartment_2:
            shared_items.append(item)
            break

sum_of_priorities = 0
for item in shared_items:
    sum_of_priorities += item_priorities[item]

print(sum_of_priorities)
