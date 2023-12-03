import re

regex = "(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))"
d = {
    "one": "1",
    "1": "1",
    "two": "2",
    "2": "2",
    "three": "3",
    "3": "3",
    "four": "4",
    "4": "4",
    "five": "5",
    "5": "5",
    "six": "6",
    "6": "6",
    "seven": "7",
    "7": "7",
    "eight": "8",
    "8": "8",
    "nine": "9",
    "9": "9",
}

file = open("input.txt", "r")
Lines = file.readlines()

total = 0
s = []
for line in Lines:
    x = re.findall(regex, line.strip())
    total += int(d[x[0]] + d[x[len(s) - 1]])
    s = []
print(total)

# 55343
