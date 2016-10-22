from parser import Parser

class Problem:
    # node = list with index along each dimension
    # common nodes can be accessed with index of any one of its node

    # size = list of no. of grids in each dimension
    # start = list with index along each dimension
    # goals = nodes treated as one
    # cost = list containing cost; size of the space
    def __init__(self, size, start, goals, cost, backward=0):
        self.size = size
        self.start = start
        self.goals = goals
        self.cost = cost
        if len(self.size) == 2:
            self.succ = [[1,0],[0,1],[-1,0],[0,-1]]
        if len(self.size) == 3:
            if backward == 1:
               self.succ = [[1,0,-1],[0,1,-1],[-1,0,-1],[0,-1,-1],[0,0,-1]]
            else:
               self.succ = [[1,0,1],[0,1,1],[-1,0,1],[0,-1,1],[0,0,1]]
        # print size
        # print start
        # print goals
        # print cost

    # returns a list of successors
    # row in the list is appended with edge cost
    def get_successors(self, node):
    # eg. for 3-d (successor_node,<edge_cost>,action)
        successors = []
        for action in range(len(self.succ)):
            successor = [x + y for x, y in zip(node, self.succ[action])]
            run_continue = 0
            for i in range(len(self.size)):
                if successor[i]<0 or successor[i]>=self.size[i]:
                    run_continue = 1
            if run_continue == 1:
                continue;
            cost = self.cost[successor[0]][successor[1]]
            successor = [successor, cost, action]
            successors.append(successor)
        return successors

    def get_node_id(self, node):
        node_id = 0
        for i in range(len(self.size)-1, -1, -1):
            num = 1
            for j in range(i):
                num = num * self.size[j]
            node_id = node_id + num*node[i]
        return node_id
