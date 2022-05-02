# Khaoula Ait Soussi : 79155

import sys
# This program checks if a graph is a collection of cycles and stars
# We first read from an input file the number of edges and vertices and the edges of the graph
# Then we create an fill in an adjacency list whose number of rows is the number of vertices
# We then check if the graph is a collection of cycles and starts. If it is, we display the number of stars and cycles and their sizes
# For stars, any vertex that is of degree greater than 2, is assumed to be a star center, and then its neighbors are checked if they're of degree 1 or not
# After finding all the stars, the remaining vertices mush all be of degree 2, if that's the case, they are traversed to find how many cycles there are
# We display a selected starting vertex of a cycle, but there might be many starting vertices for every cycle
# I used sys.exit() to terminate the program in case the graph entered is ruled out, that is why the sentence "repl process died unexpectedly" is displayed when using repl.it

# This is to read the text file as an array of lines
with open('inp.txt', 'r') as file:
  Lines = file.readlines()

# Read the number of vertices from the first line of the file/array
verts = eval(Lines[0])

# Read the number of edges from the second line of the file/array
edges = eval(Lines[1])

# Create an adjacency list that has empty rows. The number of rows is the number of vertices
# Here the index of each row represents a vertex, and each row represents the adjacency list of that vertex
adjLst = [list() for i in range(verts)]

# Fill in the adjacency list while asking the user for edges in the format a b
for i in range(2, len(Lines)):
  a,b = Lines[i].split(" ")
  a = eval(a)
  b = eval(b)
  # Whenever an edge is read from the file/array, we append its vertices to the corresponding rows in the adjacency list
  adjLst[a-1].append(b-1)   
  adjLst[b-1].append(a-1)

# Checking for stars and doing some prep-work for cycles
# For each vertex that has 3 or more adjacent vertices, check if its adjacent vertices are of degree 1
visited = 0   # This counts the number of vertices visited so far
stars = 0
twoDegVer = []    # This array stores two degree vertices
for i in range(verts):
  if(len(adjLst[i]) == 2):
    twoDegVer.append(i)
  elif (len(adjLst[i]) >= 3):   # Here is the case of a potential center of a star
    starSize = 0
    visited += 1 
    for j in range(len(adjLst[i])):
      if(len(adjLst[adjLst[i][j]]) == 1):   # This is to check if a vertex that it adjacent to the potential center is of degree 1
        visited += 1
        starSize += 1
      else:
        print("The graph is not a collection of stars and cycles! Because a vertex that is adjacent to a potential star-center is not of degree 1")
        sys.exit()
    stars += 1
    adjLst[i].append(starSize)  # This stores the size of each star at the end ot its center's adjacency list

twoDegCount = len(twoDegVer)

# check if all the non-visited vertices are of degree 2 ==> to form cycles
if(twoDegCount != verts - visited):
  print("The graph is not a collection of stars and cycles! because there is at least one vertex that does not belong to neither a star nor a cycle!")
  sys.exit()

# If the remaining vertices (i.e., unvisited) are all of degree 2, that means there are only cycles left
closedCycle = 0   # This is to count the number of cycles so far
if(twoDegCount != 0):
  visited = 1
  while(visited != twoDegCount-1):    # This is to make sure that all degree 2 vertices are visited
    start = twoDegVer[0]    # This assigns the start of the first cycle to the first 2-degree vertex in the array twoDegVer
    prev_ver = start
    next_ver = adjLst[start][0]
    twoDegVer.remove(next_ver)    # Here whenever a 2-degree vertex is visited, we remove it from the array twoDegVer so that we can easily access the start of the next cycle
    current_ver = next_ver
    cycleDeg = 0
    while(current_ver != start):
      for i in range(2):
        if(adjLst[current_ver][i] != prev_ver):
          next_ver = adjLst[current_ver][i]
          break
      visited += 1
      cycleDeg += 1
      twoDegVer.remove(next_ver)
      prev_ver = current_ver
      current_ver = next_ver
    closedCycle += 1
    adjLst[start].append(cycleDeg)    # This stores the size of each cycle at the end of its starting vertex

print("Number of Stars: ", stars)
for i in range(verts):
  length = len(adjLst[i])
  if(length > 3):
    print("\tStar ==> Center: ", i+1 ," Size: ", adjLst[i][length-1])

print("Number of Cycles: ", closedCycle)
if(closedCycle != 0):
  for i in range(verts):
    length = len(adjLst[i])
    if(length == 3):
      print("\tCycle ==> Start: ", i+1 ," Size: ", adjLst[i][length-1] + 1)
