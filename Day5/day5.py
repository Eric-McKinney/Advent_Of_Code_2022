
with open("input.txt", "r") as f:
    data = f.readlines()

initial_crates_drawing = data[:8]
stackNumbers = data[8]
moves = data[10:]


# getting indexes of each stack since number is aligned with stack
stackNumberIndexes = {}
numOfStacks = 0
for idx, character in enumerate(stackNumbers):
    if character.isdigit():
        stackNumberIndexes[character] = idx

        # the last stack number is the amount of stacks
        if len(stackNumbers) - (idx + 1) <= 2:
            numOfStacks = int(character)


initial_crates = []
for line in initial_crates_drawing:
    for idx, character in enumerate(line):
        if character.isalp():
            pass

