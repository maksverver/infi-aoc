#!/usr/bin/env python3

from machine import Program
from floodfill import FloodFill

# Lees het programma in:
with open('input.txt') as file:
    program = Program(file)

# Deel 1: bereken de som van de waarden van alle blokjes, door het programma
# voor alle coördinaten uit te voeren. De som van de waarden is het antwoord
# voor deel 1, en we houden tegelijk de coördinaten met positieve waarden bij
# in `voxels` omdat we die nodig hebben bij deel 2.

voxels = set()

answer1 = 0
for x in range(30):
    for y in range(30):
        for z in range(30):
            value = program.Execute(x, y, z)
            answer1 += value
            if value > 0:
                voxels.add((x, y, z))
print(answer1)

# Deel 2: tel de wolken, door vanaf elk punt dat tot een wolk behoort een flood
# fill uit te voeren om alle punten binnen diezelde wolk te identificeren.

def AdjacentPoints(p):
    return {p[:i] + (v + delta,) + p[i+1:] for i, v in enumerate(p) for delta in (-1, +1)}
    
def Neighbors(p):
    return AdjacentPoints(p) & voxels

clouds = set()
answer2 = 0
for p in voxels:
    if p not in clouds:
        clouds |= FloodFill(p, Neighbors)
        answer2 += 1
print(answer2)
