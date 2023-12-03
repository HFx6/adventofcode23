import re

regex = "([0-9*]+) (red|green|blue)"
id = "(Game )([0-9]+)"

file = open("input.txt", "r")
Lines = file.readlines()

total = 0
for line in Lines:
    cc = {"red": 0, "green": 0, "blue": 0}
    x = re.findall(regex, line)
    for i in x:
        cc[i[1]] = max(cc[i[1]], int(i[0]))
    if cc["red"] <= 12 and cc["green"] <= 13 and cc["blue"] <= 14:
        total += int(re.findall(id, line)[0][1])
print(total)

# 2879