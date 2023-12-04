import re


file = open("input.txt", "r")
lines = file.readlines()

t = 0
for i in lines:
    winning, mine = i.split(":")[1].split("|")[0], i.split(":")[1].split("|")[1]
    t += int(1 * pow(2, len(set(winning.split()) & set(mine.split())) - 1))

print(t)

# 25183
