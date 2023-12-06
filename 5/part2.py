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
largel = float("inf")

mrange = []
for si in range(0, len(seeds) - 1, 2):
    mrange.append([seeds[si], seeds[si + 1]])

mrange2 = [float("-inf"), float("inf")]
for rangevalues in intarraymap(7):
    r = [rangevalues[1], rangevalues[1] + rangevalues[2]]
    mrange2 = [max(mrange2[0], r[0]), min(mrange2[1], r[1])]

print(mrange2)

for seed in range(52510800, 52510820):
    mapnumbers = [-1, -1, -1, -1, -1, -1, -1, seed]
    for mapindex in reversed(range(1, 8)):
        for rangevalues in intarraymap(mapindex):
            ismapped = (
                rangevalues[0]
                <= mapnumbers[mapindex]
                < (rangevalues[0] + rangevalues[2])
            )
            if ismapped is False:
                mapnumbers[mapindex] = mapnumbers[mapindex]
            else:
                mapnumbers[mapindex] = mapnumbers[mapindex] + (
                    rangevalues[0] - rangevalues[2]
                )
                break
    print(mapnumbers)
    largel = min(largel, mapnumbers[-1])
print(largel)


# print(mrange)
