# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    closed = [[0] * len(grid[0]) for i in grid]
    closed[init[0]][init[1]] = 1 # set the initial position to checked


    x = init[0]
    y = init[1]
    g = 0
    
    open = [[g, x, y]]

    found = False # flag that is set when search complete
    resign = False # flag set if we can't find expand

    print 'initial open list:'
    for i in range(len(open)):
        print ' ', open[i]
    print '-----'

    while found is False and resign is False:
        #check if we still have elements on the open list
        if len(open) == 0:
            resign = True
            print 'fail'
        else:
            # remove node from list
            open.sort()
            open.reverse()
            next = open.pop()
            print 'take list item'
            print next
            x = next[1]
            y = next[2]
            g = next[0]

            # check if we are down 
            if x == goal[0] and y == goal[1]:
                found = True
                print next
                print 'search successful'
            else:
                # expand winning element and add to new open list
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            print 'append list item'
                            print [g2, x2, y2]
                            closed[x2][y2] = 1 # never expand agin

search(grid,init,goal,cost)

# This is my former solution
# def search(grid,init,goal,cost):
#     # ----------------------------------------
#     # insert code here
#     # ----------------------------------------
#     open = []
#     path = []
#     occupied = grid

#     open.append(init)
#     g_goal = 0
#     while open:

#         cur = open.pop()
#         if occupied[cur[0]][cur[1]] == 1:
#             continue
        
#         if cur[0] == goal[0] and cur[1] == goal[1]:
#             break
#         if not cur:
#             print "Fail"
            
#         path.append([g_goal, cur[0], cur[1]])
#         g_goal += 1
#         # looking at successors
#         for direction in delta:
#             row = cur[0]+direction[0]
#             col = cur[1]+direction[1]
#             if row == goal[0] and col == goal[1]:
#                 path.append([g_goal, row, col])
#                 return path

#             if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
#                 continue
    
#             next = occupied[row][col]
#             if next != 1:
#                 open.append([row, col])

#         # check
#         occupied[cur[0]][cur[1]] = 1

 
#     return path

# print search(grid, init, goal, cost)