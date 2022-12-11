with open("input.txt", "r") as f:
    data = f.readline()

LENGTH_OF_WINDOW = 14

for i in range(LENGTH_OF_WINDOW, len(data)):
    window = data[i-LENGTH_OF_WINDOW: i]

    duplicate_checker = set()
    for character in window:
        duplicate_checker.add(character)

    if len(duplicate_checker) == LENGTH_OF_WINDOW:
        print(i)
        break
