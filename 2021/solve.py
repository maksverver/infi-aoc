from functools import cache
import sys

def ParseIngredient(part):
  n, s = part.split(' ', 1)
  return (int(n), s)

def ParseRecipe(line):
  first, rest = line.split(': ')
  return (first, [ParseIngredient(s) for s in rest.split(', ')])

recipes = {}

@cache
def NumIngredients(what):
  if what not in recipes:
    return 1
  return sum(n*NumIngredients(s) for n, s in recipes[what])

# Parse input.
first, *rest = sys.stdin.read().splitlines()
num_missing = int(first.replace('onderdelen missen', ''))
for line in rest:
  what, ingredients = ParseRecipe(line)
  assert what not in recipes
  recipes[what] = ingredients

# Things can be partitioned into materials and toys.  Materials are things that
# are used as ingredients in other things (whether they have a recipe or not).
# Toys are things that have a recipe but are not used as an ingredient.
materials = set(s for l in recipes.values() for (_, s) in l)
toys = set(s for s in recipes if s not in materials)

print('materials', materials)
print('toys', toys)

# Part 1
print(max(map(NumIngredients, toys)))

# Part 2: dynamic programming (like a change making problem)

choices = list(sorted((toy[0], NumIngredients(toy)) for toy in toys))
# Check that all initial letters are different.
assert len(choices) == len(set(ch for ch, _ in choices))

@cache
def FindSolutions(toys_left, parts_left, pos):
  if toys_left == 0 and parts_left == 0:
    return ['']

  if toys_left == 0 or parts_left == 0 or pos == len(choices):
    return []

  res = list(FindSolutions(toys_left, parts_left, pos + 1))
  ch, n = choices[pos]
  if n <= parts_left:
    res.extend(ch + s for s in FindSolutions(toys_left - 1, parts_left - n, pos))
  return res

#print(FindSolutions(3, num_missing, 0))  # for sample
answer, = FindSolutions(20, num_missing, 0)
print(answer)
