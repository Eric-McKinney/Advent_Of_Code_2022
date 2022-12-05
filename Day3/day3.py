
with open("input.txt", "r") as f:
    data = f.readlines()

items = [i for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
priorities = [p for p in range(1,53)]
item_priorities = dict(zip(items, priorities))


def find_common_item(elves: list) -> str:
    elf1 = elves[0]
    elf2 = elves[1]
    elf3 = elves[2]
    for item in elf1:
        if item in elf2 and item in elf3:
            return item


badges = []
elf_group = []
for idx, line in enumerate(data):
    match (idx % 3):
        case 0 | 1:
            elf_group.append(line)
        case 2:
            elf_group.append(line)
            badge = find_common_item(elf_group)
            badges.append(badge)
            elf_group.clear()
        case _:
            print("Default case triggered somehow")

sum_of_priorities = 0
for badge in badges:
    sum_of_priorities += item_priorities[badge]

print(sum_of_priorities)
