from collections import Counter

import re

#data = '[0,0][1,1](1,0)(0,-1)(0,1)(-1,0)(-1,0)(0,1)(0,-1)(1,0)'  # sample
data = open('input.txt', 'rt').read()

positions = [(int(x), int(y)) for (x, y) in re.findall(r'\[(.*?),(.*?)\]', data)]
moves     = [(int(x), int(y)) for (x, y) in re.findall(r'\((.*?),(.*?)\)', data)]

n = len(positions)
collisions = 0
occupied = Counter(positions)
for i, (dx, dy) in enumerate(moves):
  if (dx, dy) == (0, 0):
    continue
  bot = i % n
  x, y = positions[bot]
  assert occupied[x, y] > 0
  occupied[x, y] -= 1
  x += dx
  y += dy
  if occupied[x, y]:
    collisions += 1

  occupied[x, y] += 1
  positions[bot] = x, y


print(collisions)
