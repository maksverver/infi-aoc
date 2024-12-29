# Infi Advent of Code 2020
# https://aoc.infi.nl/2020

# Given an octagonal shape with side length x, we can divide it into 9 equal
# parts of size x*x. For example for x=3 below:
#
#      |___|
#     /|...|\
#    /.|...|.\
#   /..|...|..\
# -----+---+-----
#  |...|...|...|
#  |...|...|...|
#  |...|...|...|
# -----+---+-----
#   \..|...|../
#    \.|...|./
#     \|...|/
#      |¯¯¯|
#
# Then we have we have five squares with occupied area x^2, and four triangles
# with occupied area x(x - 1)/2. The formula for the area thus becomes:
#
#  5x^2 + 4x(x - 1)/2 =
#  5x^2 + 2x(x - 1)   =
#  5x^2 + 2x^2 - 2x   =
#  7x^2 - 2x =
#  x(7x - 2)
#
# The formula for the circumference is simply 8x.

def Area(size):
  return size*(7*size - 2)

def Circumference(size):
  return 8*size

def GetSize(pop):
  # Find the minimum size such that Area(size) >= pop.
  #
  # We could use binary search here, or even use a closed form solution to the
  # quadratic equation 7x^2 - 2x = pop, but this is plenty fast.
  size = 1
  while Area(size) < pop:
    size += 1
  return size

# Part 1
population = 17474944
print(GetSize(population))

# Part 2
populations = [
 4_541_396_896,
 1_340_812_277,
   747_701_769,
   430_855_650,
   368_995_941,
    42_712_683,
]
for pop in populations:
  size = GetSize(pop)
  print(pop, size, Area(size - 1), Area(size))
  assert Area(size - 1) < pop < Area(size)
print(sum(Circumference(GetSize(pop)) for pop in populations))

print(*(GetSize(pop) for pop in populations))
