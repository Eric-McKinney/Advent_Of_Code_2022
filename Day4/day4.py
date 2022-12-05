
with open("input.txt", "r") as f:
    data = f.readlines()

overlappingAssignments = 0
for line in data:
    assignmentPair = line.split(",")
    assignment1 = assignmentPair[0].split("-")
    assignment2 = assignmentPair[1].split("-")

    assign1_lower_limit = int(assignment1[0])
    assign1_upper_limit = int(assignment1[1])

    assign2_lower_limit = int(assignment2[0])
    assign2_upper_limit = int(assignment2[1])

    if (assign1_lower_limit <= assign2_upper_limit and assign1_upper_limit >= assign2_lower_limit) or \
       (assign2_lower_limit <= assign1_upper_limit and assign2_upper_limit >= assign1_lower_limit):
        overlappingAssignments += 1

print(overlappingAssignments)
