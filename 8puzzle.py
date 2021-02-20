#####print table#####
def printTable(t):
  for i in range(len(t)):
    for j in range(len(t[i])):
      print(t[i][j], end = ' ')
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
  return h;

#####Node#####
  

#####goal#####
g = [[1, 2, 3], [4, 5, 6,], [7, 8, 0]]


#####main#####
#input
row1 = [int(item) for item in input('Enter 3 numbers for row 1: ').split()]
row2 = [int(item) for item in input('Enter 3 numbers for row 2: ').split()]
row3 = [int(item) for item in input('Enter 3 numbers for row 3: ').split()]

#create puzzle
t = [row1, row2, row3] #t for table
printTable(t)

h = misplacedTiles(t, g)
print(h)

if t == g:
  print("True")
else:
  print("False")

s = set()
s = t
print(s)


