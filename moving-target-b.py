import sys
import time
from problem import Problem
from parser import Parser
from planner import Planner
from dijkstra import Dijstra

# Parse variables
# filename = 'problem_1.txt'
filename = sys.argv[1]
parser = Parser(filename)

# Define Problem
N = parser.get_N()
start = parser.get_R()
start.append(0)
goals = parser.get_T()
cost = parser.get_B()
size = [N, N, len(goals)]
prob = Problem(size, start, goals, cost)

# Get heuristic from Djistra
t = time.time()
goals2d = []
for goal in goals:
    goals2d.append(goal[0:2])
prob2d = Problem(size[0:2], start[0:2], goals2d, cost)
dij = Dijstra(prob2d)
heuristic = dij.get_cost()
for i in range(len(heuristic)):
    for j in range(len(heuristic[0])):
        heuristic[i][j] = heuristic[i][j]-cost[i][j]
# for cs in heuristic:
    # print cs

# Run AStar
planner = Planner(prob, heuristic, 10)
path = planner.get_path()
elapsed = time.time() - t

# Display Output
print "Time = " + str(elapsed)
path_cost = 0
for n in path:
    if n[1] != start:
        path_cost = path_cost + cost[n[1][0]][n[1][1]]
    # print n
print "Path Cost = " + str(path_cost)
print "Path = "
for n in path:
    print n[1][0:2]
