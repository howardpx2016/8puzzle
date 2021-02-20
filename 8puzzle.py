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

#####global variables#####
solution = [[1, 2, 3], [4, 5, 6,], [7, 8, 0]]
visitedNodes = set()
expandedNodes = set()
frontier = []
maxQueueSize = 0
duplicate = []

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
    g = curr.g + 1
    if (algChoice == 1):
      h = 0
    elif (algChoice == 2):
      h = misplacedTiles(duplicate, solution)
    
    f = g + h
    newNode = Node(duplicate, f, g, h, curr)
    frontier.append(newNode)
    expandedNodes.add(newNode)

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
  maxQueueSize = len(frontier)

  # node1 = Node(problem, 5, 2, 1, None)
  # node2 = Node(problem, 2, 1, 1, node1)
  
  # frontier = [node1, node2]


  frontier.append(Node(problem, 0, 0, 0, None))
  first = frontier[0]

  while len(frontier) > 0:
    curr = frontier[0]
    frontier.pop(0)
    expandedNodes.add(curr)
    #if found, return curr
    if curr.state == solution:
      # print("right")
      return curr
    else:
      r, c = findBlank(curr.state) 
      ###operations###
      #up
      duplicate = copy.deepcopy(curr.state)
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

      ###sort frontier based on f(n)###
      frontier.sort(key = lambda Node: Node.f)
      # #test
      # for item in frontier:
      #   printNode(item)
      # print()

      if (len(frontier) > maxQueueSize):
        maxQueueSize = len(frontier)
      visitedNodes.add(curr)

      return Node(duplicate, 1, 1, 1, None)

  return problem
  


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

tick = time.perf_counter()
test = generalSearch(problem, solution, algChoice)
tock = time.perf_counter()
totalTime = tock - tick

# #test
# print("attempted puzzles:")
# for item in visitedNodes:
#   printTable(item.state)

# print("max Queue Size: ", maxQueueSize)
# print("number of puzzles assessed: ", len(visitedNodes))
# print("number of expanded nodes", len(expandedNodes), '\n')
# print("expanded Nodes:")
# for item in expandedNodes:
#   printNode(item)

printTable(test.state)
print(totalTime)


