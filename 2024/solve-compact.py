#!/usr/bin/env python3

# Lees de instructies in.
with open('input.txt') as file:
    instructions = [line.lower().split() for line in file]

# Voert het programma uit met de gegeven beginwaarden van de registers,
# en retourneert het argument van de `ret` instructie op het einde.
def RunProgram(x, y, z):
    ip = 0
    stack = []
    while 0 <= ip < len(instructions):
        cmd, *args = instructions[ip]
        ip += 1
        if cmd == 'push':
            arg, = args
            if arg == 'x':
                stack.append(x)
            elif arg == 'y':
                stack.append(y)
            elif arg == 'z':
                stack.append(z)
            else:
                stack.append(int(arg))
        elif cmd == 'add':
            assert not args
            stack.append(stack.pop() + stack.pop())
        elif cmd == 'jmpos':
            arg, = args
            if stack.pop() >= 0:
                ip += int(arg)
        elif cmd == 'ret':
            assert not args
            return stack.pop()
        else:
            raise ValueError(f'Invalid instruction on line {ip}')

# Deel 1: bereken de som van de waarden van alle blokjes,
# door het programma voor alle coördinaten uit te voeren.

voxels = {(x, y, z): RunProgram(x, y, z)
          for x in range(30)
          for y in range(30)
          for z in range(30)}

print(sum(voxels.values()))

# Deel 2: tel de wolken, door vanaf elk 3D punt dat tot een wolk behoort een
# 3D flood fill uit te voeren om alle punten binnen diezelde wolk te
# identificeren.

points = {p for p, v in voxels.items() if v > 0}

done = set()

def FloodFill(start):
    todo = [start]
    for x, y, z in todo:
        for p in ((x + 1, y, z), (x, y + 1, z), (x, y, z + 1),
                  (x - 1, y, z), (x, y - 1, z), (x, y, z - 1)):
            if p in points and p not in done:
                todo.append(p)
                done.add(p)

clouds = 0
for p in points:
    if p not in done:
        clouds += 1
        FloodFill(p)
print(clouds)
