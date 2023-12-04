import re


file = open("input.txt", "r")
lines = file.readlines()

symbols = "!@#$%^&*()_+-=[]';/"
t = 0
for i, x in enumerate(lines):
    iter = re.finditer(r"\d+", x.strip())
    indices = [[int(m.start(0)), int(m.end(0) - 1)] for m in iter]
    for k in indices:
        for p in x[max(k[0] - 1, 0) : min(k[1] + 2, len(x) - 1)]:
            if not p.isnumeric() and p != ".":
                t += int(x[k[0] : k[1] + 1])
                break
        for l in lines[min(i + 1, len(lines) - 1)][
            max(k[0] - 1, 0) : min(k[1] + 2, len(x) - 1)
        ]:
            if not l.isnumeric() and l != ".":
                t += int(x[k[0] : k[1] + 1])
                break
        for m in lines[i - 1][max(k[0] - 1, 0) : min(k[1] + 2, len(x) - 1)]:
            if not m.isnumeric() and m != ".":
                t += int(x[k[0] : k[1] + 1])
                break
print(t)

# 525911
