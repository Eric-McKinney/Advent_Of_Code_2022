with open("input.txt", "r") as f:
    data = f.readline()

for i in range(4, len(data)):
    window = data[i-4: i]

    duplicate_checker = set()
    for character in window:
        duplicate_checker.add(character)

    if len(duplicate_checker) == 4:
        print(i)
        break
