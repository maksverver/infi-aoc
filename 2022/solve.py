import sys

dirs = [
  (-1,  0),   # North
  (-1,  1),   # North East
  ( 0,  1),   # East
  ( 1,  1),   # South East
  ( 1,  0),   # South
  ( 1, -1),   # South West
  ( 0, -1),   # West
  (-1, -1),   # North West
]

dir = 0
r = c = 0
visited = set([(r, c)])
for line in sys.stdin:
  op, arg = line.split()
  arg = int(arg)
  if op == 'draai':
    assert arg % 45 == 0
    dir = (dir + arg // 45) % 8
  elif op == 'loop':
    dr, dc = dirs[dir]
    for i in range(arg):
      r += dr
      c += dc
      visited.add((r, c))
  elif op == 'spring':
    dr, dc = dirs[dir]
    r += dr*arg
    c += dc*arg
    visited.add((r, c))
  else:
    assert False

# Deel 1
print(abs(r) + abs(c))

# Deel 2
min_r = min(r for (r, c) in visited)
max_r = max(r for (r, c) in visited)
min_c = min(c for (r, c) in visited)
max_c = max(c for (r, c) in visited)
for r in range(min_r, max_r + 1):
  print(''.join('.#'[(r, c) in visited] for c in range(min_c, max_c + 1)))
