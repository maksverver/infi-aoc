maze = '''
╔═╩╗╣║╣╩║╔╝╚╝╔╦╝╔╔╝═
╚╦╦╗╗══╝═╝╦╔╣╠╩═╗╬╗╩
╩╔╦╚╗╣╗║═╦═╣╗╣║╦╔═╦╩
╠╗═╬╣╦╚╠╔║╠╠║╗╣╔╠╔═╝
╦═╗╣║╦╚╦╬║╣╝═╩╠╠═╔╩║
╚═╗╦║═║╦═╝╗╣╦═╠╦║╦╠╗
╚╠╩╗╠╔╬═╗╚╣╔║╣╔╝╦═╗╝
╩╚╣═╬╦║║╣╣╦╝╩╗╚╚╝║╠╝
╣╝║╠╩╣╩║║╝═╔╣═╠╗║╩╦═
╣║╠║╠╠═║╠╗╣╗╩╝╩╗╝║║╝
╬╣╚╗╚╚╗╦╬╗╠╗╚══╗║╩╬═
╩║═╠╦╗╚╗╬║╦╚║╩╠╚╝═╔═
║╝╝╦╚║╚║╔╚╠╚═╦╣║╝╔╝╚
╝╦╬╝╦╔═╬╗╝║╗║╠╗╚║║═╣
║╗╬╗╗╦╝╠╣╝╦╣║╩╣╚╗╚╚║
╬╔╗║╣╝╬╔╚╦╣╬═╗╬║║╝╩╠
╔╠║╬╔╚╩═╣╬╣║╚║╣╦╔═╣╣
╔╦╠╔╦╚═╦╝╚╬╝╩╬╚╗╝╩╣╚
╗╔═╩═╩╣╔╔╚╔║╣║╩╩╩╔╚═
╣║╔╦╚╣╚╝╔╝╔╣╠╩╦╬══╩╝
'''.split()

# Example input
# maze = '''
# ╔═╗║
# ╠╗╠║
# ╬╬╣╬
# ╚╩╩═
# '''.split()

exits = {
  #     UP        LEFT      RIGHT     DOWN
  '║': [(-1,  0),                     ( 1,  0)],
  '╔': [                    ( 0,  1), ( 1,  0)],
  '╗': [          ( 0, -1),           ( 1,  0)],
  '╠': [(-1,  0),           ( 0,  1), ( 1,  0)],
  '╦': [          ( 0, -1), ( 0,  1), ( 1,  0)],
  '╚': [(-1,  0),           ( 0,  1)          ],
  '╝': [(-1,  0), ( 0, -1)                    ],
  '╬': [(-1,  0), ( 0, -1), ( 0,  1), ( 1,  0)],
  '╩': [(-1,  0), ( 0, -1), ( 0,  1)          ],
  '═': [          ( 0, -1), ( 0,  1)          ],
  '╣': [(-1,  0), ( 0, -1),           ( 1,  0)],
}

H = len(maze)
W = len(maze[0])

def Part1():
  # Breadth-first search through the maze
  todo = [(0, 0)]
  dist = {(0, 0): 0}
  i = 0
  while i < len(todo):
    r, c = todo[i]
    i += 1
    for dr, dc in exits[maze[r][c]]:
      rr, cc = r + dr, c + dc
      if 0 <= rr < H and 0 <= cc < W and (-dr, -dc) in exits[maze[rr][cc]] and (rr, cc) not in dist:
        dist[rr, cc] = dist[r, c] + 1
        todo.append((rr, cc))
  return dist[H - 1, W - 1]


def Transform(r, c, t, maze):
  maze = [list(row) for row in maze]
  if t % 2 == 0:
    rr = t % H
    if r == rr: c = (c + 1) % W
    maze[rr] = maze[rr][-1:] + maze[rr][:-1]
  else:
    cc = t % W
    if c == cc: r = (r + 1) % H
    col = [maze[rr][cc] for rr in range(H)]
    col = col[-1:] + col[:-1]
    for rr in range(H):
      maze[rr][cc] = col[rr]
  return (r, c, t + 1, tuple(''.join(row) for row in maze))


def Part2():
  # Breadth-first search through the maze as it changes.
  # State is (row, column, time, maze)
  initial = (0, 0, 0, tuple(maze))
  todo = [initial]
  dist = {initial: 0}
  i = 0
  while i < len(todo):
    state = todo[i]
    r, c, t, m = state
    i += 1
    for dr, dc in exits[m[r][c]]:
      rr, cc = r + dr, c + dc
      if 0 <= rr < H and 0 <= cc < W and (-dr, -dc) in exits[m[rr][cc]]:
        if (rr, cc) == (H - 1, W - 1):
          return dist[r, c, t, m] + 1  # Solution found!
        next_state = Transform(rr, cc, t, m)
        if next_state not in dist:
          dist[next_state] = dist[state] + 1
          todo.append(next_state)

print(Part1())
print(Part2())
