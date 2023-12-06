import re


file = open("input.txt", "r")
lines = file.read()

groups = lines.split("\n\n")
seeds = [int(x) for x in groups[0].split()[1:]]


def intarraymap(index):
    return [
        [int(item) for item in sublist]
        for sublist in [i.split() for i in groups[index].split("\n")[1:]]
    ]


d = {}
largel = float('inf')


for seed in seeds:
    mapnumbers = [seed, -1, -1, -1, -1, -1, -1, -1]
    for mapindex in range(1, 8):
        for rangevalues in intarraymap(mapindex):
            ismapped = (
                rangevalues[1]
                <= mapnumbers[mapindex - 1]
                < (rangevalues[1] + rangevalues[2])
            )
            if ismapped is False:
                mapnumbers[mapindex] = mapnumbers[mapindex - 1]
            else:
                r = mapnumbers[mapindex - 1] + (
                    rangevalues[0] - rangevalues[1]
                )
                mapnumbers[mapindex] = mapnumbers[mapindex - 1] + (
                    rangevalues[0] - rangevalues[1]
                )
                break
    largel = min(largel, mapnumbers[-1])
print(largel)


# 662197086