from problem import Problem
from parser import Parser

# Parse variables
filename = 'problem_0.txt'
parser = Parser(filename)

# Define Problem
N = parser.get_N()
start = parser.get_R()
start.append(0)
goals = parser.get_T()
cost = parser.get_B()
size = [N, N, len(goals)]
prob = Problem(size, start, goals, cost, 1)

# Test
print prob.get_successors_with_cost([3,3,6])
print prob.get_node_id([1,1,0])
