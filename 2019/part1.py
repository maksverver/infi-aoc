flats = [[2,10],[4,5],[9,4],[11,5],[12,6],[13,9],[16,9],[20,8],[21,10],[25,8],[27,10],[32,10],[34,9],[36,7],[38,10],[42,9],[43,10],[44,8],[47,10],[50,8],[51,8],[55,3],[59,4],[60,7]]
jumps = [[1,0],[4,0],[1,1],[0,1],[0,3],[2,0],[3,0],[0,2],[3,0],[1,2],[4,0],[0,0],[1,0],[1,3],[3,0],[0,1],[0,0],[2,2],[2,0],[0,0],[3,0],[3,1],[0,3]]

# Sample data
# flats = [[1,4],[3,8],[4,3],[5,7],[7,4],[10,3]]
# jumps = [[2,0],[0,4],[1,0],[0,0]]

answer = 0
pos = 0
for dx, dy in jumps:
  answer += 1
  x, y = flats[pos]
  x += dx + 1
  y += dy
  while pos < len(flats) and flats[pos][0] < x:
    pos += 1
  if pos == len(flats) or flats[pos][0] != x or flats[pos][1] > y:
    break
print(answer)