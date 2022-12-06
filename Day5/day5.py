
with open("input.txt", "r") as f:
    data = f.readlines()

initial_crates = data[:8]
moves = data[10:]

initial_state = []
for line in initial_crates:
    crates = []
    for character in line:
        if character.isalpha():
            crates.append(character)
