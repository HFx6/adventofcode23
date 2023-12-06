from functools import reduce

file = open("input.txt", "r")
lines = file.readlines()

time = [int(x) for x in lines[0].split()[1:]]
distance = [int(x) for x in lines[1].split()[1:]]

d = [0]*len(time)

for i in range(0, len(time)):
    for j in range(0, time[i]):
        p = time[i] - j
        o = j * p
        if o > distance[i]:
            d[i] += 1
print(reduce(lambda x, y: x * y, d))

# 393120