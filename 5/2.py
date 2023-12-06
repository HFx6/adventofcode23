import re
import bisect

file = open("input.txt", "r")
lines = file.read()

groups = lines.split("\n\n")
seeds = [int(x) for x in groups[0].split()[1:]]

# Use a dictionary to store the results of intarraymap(index)
intarraymap_cache = {}

def intarraymap(index):
    if index not in intarraymap_cache:
        intarraymap_cache[index] = [
            [int(item) for item in sublist]
            for sublist in [i.split() for i in groups[index].split("\n")[1:]]
        ]
    return intarraymap_cache[index]
for mapindex in [7, 6, 5, 4, 3, 2, 1]:
    intarraymap(mapindex)
d = -1
largel = float("inf")

mrange = []
for si in range(0, len(seeds) - 1, 2):
    mrange.append([seeds[si], seeds[si] + seeds[si + 1]])

for l in range(0, 4000000000):
    mapnumbers = [-1, -1, -1, -1, -1, -1, -1, -1, l]
    for mapindex in [7, 6, 5, 4, 3, 2, 1]:        
        for rangevalues in intarraymap_cache[mapindex]:
            ismapped = (
                rangevalues[0]
                <= mapnumbers[mapindex + 1]
                < (rangevalues[0] + rangevalues[2])
            )

            if ismapped is False:
                mapnumbers[mapindex] = mapnumbers[mapindex + 1]
            else:
                mapnumbers[mapindex] = mapnumbers[mapindex + 1] + (
                    rangevalues[1] - rangevalues[0]
                )
                break
    if l == 662197086:
        print(l)
    for m in mrange:
        if m[0] <= mapnumbers[1] < m[1]:
            d = mapnumbers[-1]
    if d != -1:
        break

print(d)