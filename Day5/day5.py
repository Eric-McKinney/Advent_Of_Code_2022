
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


stacks = []
for i in range(num_of_stacks):
    stacks.append([])


unparsed_crates_drawing.reverse() # starts adding to stacks from bottom up
for line in unparsed_crates_drawing:
    for idx, character in enumerate(line):
        if character.isalpha():
            stack_num = stack_number_indexes[idx]
            stacks[stack_num].append(character)


def move_crates(amount, start, destination):
    crate_buffer = []
    for crate_num in range(amount):
        crate = stacks[start - 1].pop()
        crate_buffer.append(crate)

    crate_buffer.reverse()
    for item in crate_buffer:
        stacks[destination - 1].append(item)


for line in moves:
    parsing_index = 5
    amount_of_crates = int(line[parsing_index])
    if line[parsing_index + 1].isdigit():
        amount_of_crates = int(line[parsing_index: parsing_index + 2])
        parsing_index += 1

    parsing_index += 7
    starting_stack = int(line[parsing_index])
    if line[parsing_index + 1].isdigit():
        starting_stack = int(line[parsing_index: parsing_index + 2])
        parsing_index += 1

    parsing_index += 5
    ending_stack = int(line[parsing_index])
    if line[parsing_index + 1].isdigit():
        ending_stack = int(line[parsing_index: parsing_index + 2])

    move_crates(amount_of_crates, starting_stack, ending_stack)

top_crates = ""
for stack in stacks:
    top_crates += stack[-1]

print(top_crates)
