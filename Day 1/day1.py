
with open("data.txt", "r") as f:
    data = f.readlines()

calorie_sums = []
sum_calories = 0
for line in data:
    if line != "\n":
        sum_calories += int(line)
    else:
        calorie_sums.append(sum_calories)
        sum_calories = 0

calorie_sums.sort(reverse=True)
sum_top_3 = calorie_sums[0] + calorie_sums[1] + calorie_sums[2]
print(sum_top_3)
