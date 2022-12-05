
with open("input.txt", "r") as f:
    data = f.readlines()

overlappingAssignments = 0
for line in data:
    assignmentPair = line.split(",")

