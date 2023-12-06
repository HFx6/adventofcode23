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


stsm = intarraymap(1)
stfm = intarraymap(2)
ftwm = intarraymap(3)
wtlm = intarraymap(4)
lttm = intarraymap(5)
tthm = intarraymap(6)
htlm = intarraymap(7)

zstsm = ""
zstfm = ""
zftwm = ""
zwtlm = ""
zlttm = ""
ztthm = ""
zhtlm = ""

for i in stsm:
    z = zip(range(i[1], i[1] + i[2]), range(i[0], i[0] + i[2]))
    zstsm = [*list(z), *zstsm]

for i in stfm:
    z = zip(range(i[1], i[1] + i[2]), range(i[0], i[0] + i[2]))
    zstfm = [*list(z), *zstfm]

for i in ftwm:
    z = zip(range(i[1], i[1] + i[2]), range(i[0], i[0] + i[2]))
    zftwm = [*list(z), *zftwm]

for i in wtlm:
    z = zip(range(i[1], i[1] + i[2]), range(i[0], i[0] + i[2]))
    zwtlm = [*list(z), *zwtlm]

for i in lttm:
    z = zip(range(i[1], i[1] + i[2]), range(i[0], i[0] + i[2]))
    zlttm = [*list(z), *zlttm]

for i in tthm:
    z = zip(range(i[1], i[1] + i[2]), range(i[0], i[0] + i[2]))
    ztthm = [*list(z), *ztthm]

for i in htlm:
    z = zip(range(i[1], i[1] + i[2]), range(i[0], i[0] + i[2]))
    zhtlm = [*list(z), *zhtlm]
d = {}
for i in seeds:
    d = {
        "seed": i,
        "soil": -1,
        "fertilizer": -1,
        "water": -1,
        "light": -1,
        "temperature": -1,
        "humidity": -1,
        "location": -1,
    }
    for l in zstsm:
        if l[0] == i:
            d["soil"] = l[1]
    if d["soil"] == -1:
        d["soil"] = i

    for l in zstfm:
        if l[0] == d["soil"]:
            d["fertilizer"] = l[1]
    if d["fertilizer"] == -1:
        d["fertilizer"] = d["soil"]

    for l in zftwm:
        if l[0] == d["fertilizer"]:
            d["water"] = l[1]
    if d["water"] == -1:
        d["water"] = d["fertilizer"]

    for l in zwtlm:
        if l[0] == d["water"]:
            d["light"] = l[1]
    if d["light"] == -1:
        d["light"] = d["water"]

    for l in zlttm:
        if l[0] == d["light"]:
            d["temperature"] = l[1]
    if d["temperature"] == -1:
        d["temperature"] = d["light"]

    for l in ztthm:
        if l[0] == d["temperature"]:
            d["humidity"] = l[1]
    if d["humidity"] == -1:
        d["humidity"] = d["temperature"]

    for l in zhtlm:
        if l[0] == d["humidity"]:
            d["location"] = l[1]
    if d["location"] == -1:
        d["location"] = d["humidity"]

    print(d)
