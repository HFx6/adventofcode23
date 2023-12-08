import collections
from bisect import bisect


file = open("input.txt", "r")
lines = file.readlines()


hand = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]

types = [[], [], [], [], [], [], []]
bets = [[], [], [], [], [], [], []]
real = [[], [], [], [], [], [], []]

for _line in lines:
    line = _line.split()

    card = line[0]
    bet = line[1]
    freq = collections.Counter(card)
    freqex = list(sorted(freq.values()))
    print(sorted(card.replace("J", ""), reverse=True)) 
    bestj = collections.Counter(sorted(card.replace("J", ""), reverse=True)).most_common()[0][0]
    print(bestj)
    cbestj = card.replace("J", bestj)
    l = hand.index(freqex)
    rep = ""
    for i in cbestj:
        if i == "T":
            rep += "V"
        elif i == "J":
            rep += "1"
        elif i == "Q":
            rep += "X"
        elif i == "K":
            rep += "Y"
        elif i == "A":
            rep += "Z"
        else:
            rep += i
    print(rep)
    jtype = card.replace("J", "1")
    index = bisect(types[l], rep)
    types[l].insert(index, jtype)
    real[l].insert(index, jtype)
    bets[l].insert(index, int(bet))

fbets = [item for row in bets for item in row]
sum = 0
for i in range(1, len(lines) + 1):
    sum += fbets[i - 1] * i
print(sum)
print(real)
# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456
