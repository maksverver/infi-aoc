from collections import Counter

import re

#data = '[0,0][1,1](1,0)(0,-1)(0,1)(-1,0)(-1,0)(0,1)(0,-1)(1,0)'
#data = open('input.txt', 'rt').read()
data = open(0).read()

positions = [(int(x), int(y)) for (x, y) in re.findall(r'\[(.*?),(.*?)\]', data)]
moves     = [(int(x), int(y)) for (x, y) in re.findall(r'\((.*?),(.*?)\)', data)]

min_x = min_y = max_x = max_y = 0

print('<svg viewBox="0 0 50 30" xmlns="http://www.w3.org/2000/svg">')

visited = Counter(positions)
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

    # for y in range(29):
    #   print(*['.#'[(x, y) in visited] for x in range(47)])
    # print()

  occupied[x, y] += 1
  positions[bot] = x, y

  # print(f'<line x1="{x-dx}" y1="{y-dy}" x2="{x}" y2="{y}" stroke="black" stroke-width="0.1" />')

  visited[x, y] += 1
  min_x = min(min_x, x)
  min_y = min(min_y, y)
  max_x = max(max_x, x)
  max_y = max(max_y, y)

print('</svg>')
assert min_x == 0
assert min_y == 0

# height = max_y - min_y + 1
# width = max_x - min_x + 1
# print(height, width)  # 29x47
# for x in range(width):
#   for y in range(height):
#     if not visited[x, y]:
#       print(x, y)
print(collisions)  # part 1



# from PIL import Image

# print(min_x, min_y, max_x, max_y)

# height = max_y - min_y + 1
# width = max_x - min_x + 1
# image = Image.new('L', (width, height))
# pixels = image.load()
# for x in range(width):
#   for y in range(height):
#     if visited[x, y] == 0:
#       print(x,y)
#     pixels[x, y] = visited[x, y]*5
# image.save('output.png')


# TODO: part 2 (geen idee wat er gevraagd wordt)
