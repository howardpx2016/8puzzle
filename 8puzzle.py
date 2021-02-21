import time
import copy

#####print table#####
def printTable(t):
  for i in range(len(t)):
    for j in range(len(t[i])):
      print(t[i][j], end = ' ')
    print()

#####print Node info#####
def printNode(node):
  print('Node info')
  print('Puzzle:')
  printTable(node.state)
  print('f(n): ', node.f)
  print('g(n): ', node.g)
  print('h(n): ', node.h)
  if (node.parent != None):
    print('Parent Node Puzzle:')
    printTable(node.parent.state)
  else: 
    print('No parent, this is the root')
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
def misplacedTiles(t, s):
  h = 0
  for i in range(len(t)):
    for j in range(len(t[i])):
      if (t[i][j] != 0) and (t[i][j] != s[i][j]):
        h += 1
  return h
def manhattan(t, s):
  distance = 0
  for i in range(len(t)):
    for j in range(len(t[i])):
      if t[i][j] != 0:
        goal_row = int((t[i][j]-1)/3)
        goal_column = (t[i][j]-1)%3
        distance += abs(goal_row - i) + abs(goal_column - j)
  return distance
  

#####global variables#####
solution = [[1, 2, 3,], [4, 5, 6,], [7, 8, 0]]
visitedNodes = set()
expandedNodes = set()
frontier = []
duplicate = []
maxQueueSize = 0

#####Node Class#####
class Node:
  def __init__(self, state, f, g, h, parent):
    self.state = state
    self.f = f
    self.g = g
    self.h = h
    self.parent = parent

#####Create New Children#####
def createChild(algChoice, curr, duplicate, frontier, visitedNodes, expandedNodes):
  if findDuplicates(visitedNodes, duplicate) == False: #set accepts new puzzle --> puzzle is unique
    f, g, h = fgh(duplicate, solution, curr)
    newNode = Node(duplicate, f, g, h, curr)
    frontier.append(newNode)
    expandedNodes.add(newNode)

#####Compute f, g, h#####
def fgh(puzzle, solution, curr):
  if curr != None:
    g = curr.g + 1
  else:
    g = 0
  if (algChoice == 1):
    h = 0
  elif (algChoice == 2):
    h = misplacedTiles(puzzle, solution)
  elif (algChoice == 3):
    h = manhattan(puzzle, solution)
  f = g + h
  return f, g, h

#####Convert list to set#####
def freeze(table):
  for rows in table:
    frozenset(rows)

#####Search for duplicates#####
def findDuplicates(visitedNodes, duplicate):
  for item in visitedNodes:
    if item.state == duplicate:
      return True
  return False

#####General Function#####
def generalSearch(problem, solution, algChoice):
  global maxQueueSize

  f, g, h = fgh(problem, solution, None)
  root = Node(problem, f, g, h, None)

  frontier.append(root)
  maxQueueSize = len(frontier)
  # print("og: ", maxQueueSize)
  expandedNodes.add(root)

  while len(frontier) > 0:
    curr = frontier[0]
    visitedNodes.add(curr)

    if (len(frontier) > maxQueueSize):
      maxQueueSize = len(frontier)
    # print("next: ", maxQueueSize)

    #if found, return curr
    if misplacedTiles(curr.state, solution) == 0:
      # print("right")
      return curr

    ####else####
    duplicate = copy.deepcopy(curr.state)
    r, c = findBlank(duplicate) 
    #operations
    #up
    
    if r > 0:
      up(duplicate, r, c)
      createChild(algChoice, curr, duplicate, frontier, visitedNodes, expandedNodes)
    #down
    duplicate = copy.deepcopy(curr.state)
    if r < 2:
      down(duplicate, r, c)
      createChild(algChoice, curr, duplicate, frontier, visitedNodes, expandedNodes)
    #left
    duplicate = copy.deepcopy(curr.state)
    if c > 0:
      left(duplicate, r, c)
      createChild(algChoice, curr, duplicate, frontier, visitedNodes, expandedNodes)
    #right
    duplicate = copy.deepcopy(curr.state)
    if c < 2:
      right(duplicate, r, c)
      createChild(algChoice, curr, duplicate, frontier, visitedNodes, expandedNodes)

    frontier.pop(0)

    ###sort frontier based on f(n)###
    frontier.sort(key = lambda Node: Node.f)

  return None
  


#####main#####
#input and create puzzle
print('Create your 3x3 puzzle. Make sure it can be solved')
print('(Use 0 as a blank, numbers 1-8 for the tiles)\n')

row1 = [int(item) for item in input('Enter 3 numbers for row 1: ').split()]
row2 = [int(item) for item in input('Enter 3 numbers for row 2: ').split()]
row3 = [int(item) for item in input('Enter 3 numbers for row 3: ').split()]
print()

print('Your puzzle is:')
problem = [row1, row2, row3] 
printTable(problem)
print()

print('Your choices of algorithms are:')
print('1. Uniform Cost Search')
print('2. A* with Misplaced Tile heuristic')
print('3. A* with Manhattan distance heuristic\n')

algChoice = int(input('Enter your algorithm of choice (1-3): '))
print()

tick = time.perf_counter()
test = generalSearch(problem, solution, algChoice)
tock = time.perf_counter()
totalTime = tock - tick

if (test == None):
  print('Solution was not Found')
else:
  print('Solution Found!')
  print('Depth: ', test.g)
  print("max Queue Size: ", maxQueueSize)
  print("number of puzzles assessed: ", len(visitedNodes))
  print("number of expanded nodes", len(expandedNodes), '\n')
  printNode(test)

print('Time elpased (seconds): ', totalTime)

# #test
# for item in expandedNodes:
#   printNode(item)