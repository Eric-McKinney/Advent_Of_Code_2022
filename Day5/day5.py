
with open("input.txt", "r") as f:
    data = f.readlines()

unparsed_crates_drawing = data[:8]
stack_numbers = data[8]
moves = data[10:]


# getting indexes of each stack since number is aligned with stack
stack_number_indexes = {}
num_of_stacks = 0
for idx, character in enumerate(stack_numbers):
    if character.isdigit():
        stack_number_indexes[idx] = int(character) - 1 # offset so it matches index

        # the last stack number is the amount of stacks
        if len(stack_numbers) - (idx + 1) <= 2:
            num_of_stacks = int(character)


initial_stacks = []
for i in range(num_of_stacks):
    initial_stacks.append([])


unparsed_crates_drawing.reverse() # starts adding to stacks from bottom up
for line in unparsed_crates_drawing:
    for idx, character in enumerate(line):
        if character.isalpha():
            stack_num = stack_number_indexes[idx]
            initial_stacks[stack_num].append(character)


