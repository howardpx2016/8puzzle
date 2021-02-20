import time

#####print table#####
def printTable(t):
  for i in range(len(t)):
    for j in range(len(t[i])):
      print(t[i][j], end = ' ')
    print()
  print()

#####operations#####
def findBlank(t):
  for i in range(len(t)):
    for j in range(len(t[i])):
      if t[i][j] == 0:
        return i, j
def up(t, r, c):
  temp = t[r][c] 
  t[r][c] = t[r-1][c]
  t[r-1][c] = temp
def down(t, r, c):
  temp = t[r][c] 
  t[r][c] = t[r+1][c]
  t[r+1][c] = temp
def left(t, r, c):
  temp = t[r][c] 
  t[r][c] = t[r][c-1]
  t[r][c-1] = temp
def right(t, r, c):
  temp = t[r][c] 
  t[r][c] = t[r][c+1]
  t[r][c+1] = temp

#####heuristics#####
def misplacedTiles(t, g):
  h = 0
  for i in range(len(t)):
    for j in range(len(t[i])):
      if (t[i][j] != 0) and (t[i][j] != g[i][j]):
        h += 1
  return h

#####solution#####
solution = [[1, 2, 3], [4, 5, 6,], [7, 8, 0]]

#####Node Class#####
class Node:
  def __init__(self, state, f, g, h, parent):
    self.state = state
    self.f = f
    self.g = g
    self.h = h
    self.parent = parent

#####General Function#####
def generalSearch(problem, solution, algChoice):
  visitedNodes = set()
  expandedNodes = set()
  attemptedPuzzles = set()
  frontier = []
  maxQueueSize = len(frontier)

  # node1 = Node(problem, 5, 2, 1, None)
  # node2 = Node(problem, 2, 1, 1, node1)
  
  # frontier = [node1, node2]
  # frontier.sort(key = lambda Node: Node.f)
  # for item in frontier:
  #   print(item.f)
  # print(f)

  return solution


#####main#####
#input and create puzzle
print('Create your 3x3 puzzle. Make sure it can be solved')
print('(Use 0 as a blank, numbers 1-8 for the tiles)\n')

row1 = [int(item) for item in input('Enter 3 numbers for row 1: ').split()]
row2 = [int(item) for item in input('Enter 3 numbers for row 2: ').split()]
row3 = [int(item) for item in input('Enter 3 numbers for row 3: ').split()]
print()

print('Your puzzle is:')
problem = set()
problem = [row1, row2, row3] 
printTable(problem)

print('Your choices of algorithms are:')
print('1. Uniform Cost Search')
print('2. A* with Misplaced Tile heuristic')
print('3. A* with Manhattan distance heuristic\n')

algChoice = int(input('Enter your algorithm of choice (1-3): '))

tick = time.perf_counter()
test = generalSearch(problem, solution, algChoice)
tock = time.perf_counter()
totalTime = tock - tick
print(test)
print(totalTime)


