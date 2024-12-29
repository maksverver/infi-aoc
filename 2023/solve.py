# Infi.nl Advent of Code
# https://aoc.infi.nl/2023

from math import hypot, inf


def Calc1(polygon):
  # Minimum radius of a circle centered at the origin that includes the entire
  # polygon. This is simply the maximum distance from any vertex to the origin.
  return max(hypot(x, y) for (x, y) in polygon)


def Part1(polygons):
  return sum(Calc1(polygon) for polygon in polygons)


def CenterOfCircumCircle(x1, y1, x2, y2, x3, y3) :
  '''Returns the center of the circumcircle of the given triangle, i.e., the
     circle that passes through all three points. The points may not be colinear.'''
  # Logic adapted from:
  # https://www.geeksforgeeks.org/equation-of-circle-when-three-points-on-the-circle-are-given/
  x12 = x1 - x2
  y12 = y1 - y2
  x13 = x1 - x3
  y13 = y1 - y3
  x21 = x2 - x1
  y21 = y2 - y1
  x31 = x3 - x1
  y31 = y3 - y1
  sx13 = x1**2 - x3**2
  sy13 = y1**2 - y3**2
  sx21 = x2**2 - x1**2
  sy21 = y2**2 - y1**2
  cx = (sx13*y12 + sy13*y12 + sx21*y13 + sy21*y13) / (x21*y13 - x31*y12) / 2
  cy = (sx13*x12 + sy13*x12 + sx21*x13 + sy21*x13) / (y21*x13 - y31*x12) / 2
  return (cx, cy)


def Calc2(polygon):
  # Returns the minimum circle that includes the entire polygon, if we can
  # choose the center freely. The minimal circle will either touch exactly two
  # points (then the center lies on the midpoint) or (at least) three points.
  # We can consider all the cases.

  best = (inf, 0, 0)

  def CalcRadius(cx, cy):
    return max(hypot(x - cx, y - cy) for (x, y) in polygon)

  for i in range(len(polygon)):
    x1, y1 = polygon[i]
    for j in range(i + 1, len(polygon)):
      x2, y2 = polygon[j]
      cx = (x1 + x2)/2
      cy = (y1 + y2)/2
      best = min(best, (CalcRadius(cx, cy), cx, cy))
      for k in range(j + 1, len(polygon)):
        x3, y3 = polygon[k]
        cx, cy = CenterOfCircumCircle(x1, y1, x2, y2, x3, y3)
        best = min(best, (CalcRadius(cx, cy), cx, cy))
  return best


def Part2(polygons):
  answer = 0
  for caseNo, polygon in enumerate(polygons):
    r, cx, cy = Calc2(polygon)
    answer += r

    if False:
      # For debugging: generate SVG to illustrate solution.
      with open('case-%d.svg' % caseNo, 'wt') as f:
        f.write(f'''\
<svg viewBox="-150 -150 300 300" xmlns="http://www.w3.org/2000/svg">
<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="blue" />
<polygon points="{' '.join(f'{x},{y}' for (x, y) in polygon)}" fill="none" stroke="black" stroke-linejoin="round" />
</svg>''')

  return answer


testdata = [
  [(10, -39), (35, -86), (-89, 13), (70, -100), (-27, -37), (97, 25), (89, -24)],
  [(88, 33), (79, 23), (7, -95), (-92, -9), (-60, -72), (18, 58)],
  [(93, -38), (62, -49), (59, -77), (-66, -50), (55, -59)],
  [(19, -20), (6, -50), (18, -85), (6, 69), (-82, 62), (45, 91)],
  [(-97, -27), (73, 1), (70, -5), (85, -7), (55, -38)],
  [(-89, 1), (45, 65), (65, -58)],
  [(-68, -9), (-54, -96), (-74, -1), (57, 73), (-76, 22)],
  [(40, 45), (-53, -30), (-44, -52), (-15, -50), (32, -20), (-40, -45)],
  [(64, -82), (-2, -61), (-84, -31)],
  [(-97, 76), (-42, 13), (0, -41), (99, -53), (-26, 43), (96, -30)],
  [(44, -86), (16, 59), (41, -55), (-3, -21)],
  [(10, -78), (71, -65), (-94, -61), (-92, -100), (18, 56)],
  [(81, 45), (64, -14), (33, 69), (96, -52), (-62, 75), (88, -16)],
  [(92, -5), (49, 1), (39, -2), (71, 71), (-40, -13), (-35, -64), (41, -36)],
  [(59, -62), (-26, -75), (-61, 14), (-19, 99)],
  [(-71, -75), (71, -52), (-51, -60), (40, 21)],
  [(81, -57), (11, -10), (6, -40), (-81, 85), (84, 20), (-43, -2)],
  [(92, 5), (44, -11), (-100, 0), (62, -56)],
  [(10, -5), (-1, -28), (13, 27), (22, 22)],
  [(47, 44), (-2, 60), (-80, 40)],
  [(31, -87), (-95, -46), (29, 61), (42, 52)],
  [(-67, -35), (4, 60), (-60, -61), (59, -7), (5, 33), (-84, 91), (-66, 47)],
  [(-38, -38), (0, 9), (54, 52), (-69, -15), (-97, -81)],
  [(-13, 56), (89, 46), (49, 53), (46, -7)],
  [(-38, -82), (62, 80), (8, 84), (-96, -45), (-14, 24)],
]

print(Part1(testdata))  # 2561.8898615822372
print(Part2(testdata))  # 2158.892834786057
