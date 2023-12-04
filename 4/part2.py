import re

file = open("input.txt", "r")
lines = file.readlines()

sum = 0

for i, x in enumerate(lines):
    gears = re.finditer(r"\*", x.strip())
    topNums = re.finditer(r"\d+", lines[i - 1].strip()) if i > 0 else []
    middleNums = re.finditer(r"\d+", lines[i].strip())
    bottomNums = re.finditer(r"\d+", lines[i + 1].strip()) if i < len(lines) - 1 else []
    nums = list(topNums) + list(middleNums) + list(bottomNums)

    for gear in gears:
        gearRange = gear.span()
        partNums = []
        for num in nums:
            numRange = num.span()
            numMatch = num.group(0)

            if numRange[0] <= gearRange[1] and gearRange[0] <= numRange[1]:
                partNums.append(numMatch)

        if len(partNums) == 2:
            sum += int(partNums[0]) * int(partNums[1])

print(sum)