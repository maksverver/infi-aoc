from math import inf

flats = [[2,10],[4,5],[9,4],[11,5],[12,6],[13,9],[16,9],[20,8],[21,10],[25,8],[27,10],[32,10],[34,9],[36,7],[38,10],[42,9],[43,10],[44,8],[47,10],[50,8],[51,8],[55,3],[59,4],[60,7]]

# Sample data
#flats = [[1,4],[3,8],[4,3],[5,7],[7,4],[10,3]]

n = len(flats)
energy = [inf]*n
energy[n - 1] = 0
for i in reversed(range(n - 1)):
  j = i + 1
  while j < n:
    e = flats[j][0] - flats[i][0] - 1
    if e > 4:
      break
    e += max(flats[j][1] - flats[i][1], 0)
    if e <= 4:
      energy[i] = min(energy[i], energy[j] + e)
    j = j + 1
print(energy)
print(energy[0])
