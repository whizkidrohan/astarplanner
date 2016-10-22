from problem import Problem
from parser import Parser
from planner import Planner
from dijkstra import Dijstra

# Parse variables
filename = 'problem_1.txt'
parser = Parser(filename)

# Define Problem
N = parser.get_N()
start = parser.get_R()
start.append(0)
goals = parser.get_T()
cost = parser.get_B()
size = [N, N, len(goals)]
prob = Problem(size, start, goals, cost)

print cost[992][967]
print cost[0][0]
# Get heuristic from Djistra
# goals2d = []
# for goal in goals:
    # goals2d.append(goal[0:2])
# prob2d = Problem(size[0:2], start[0:2], goals2d, cost)
# dij = Dijstra(prob2d)
# heuristic = dij.get_cost()
# for cs in heuristic:
    # print cs
# # # run AStar
# planner = Planner(prob, heuristic)
# path = planner.get_path()
# print "Path="
# path_cost = 0
# for n in path:
    # path_cost = path_cost + cost[n[1][0]][n[1][1]]
    # print n
# print path_cost
