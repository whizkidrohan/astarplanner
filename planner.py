from Queue import PriorityQueue
class Planner:
    # Gives a plan from start to goal

    # heuristic = an array with size of space
    # problem = object of problem class
    def __init__(self, problem):
        self.prob = problem

    def get_path(self):
        start_node = self.prob.start
        plan = []
        cost = -1
        # struct = [f, cost, node, action, parent]
        open_list = PriorityQueue()
        closed_list = {}
        cost = self.prob.cost[start_node[0]][start_node[1]]
        open_list.put([cost+self.get_heuristic(start_node), cost, start_node, \
            -1, -1])

        while open_list:
            # for l in open_list.queue:
                # print l
            current_struct = open_list.get()
            if self.prob.get_node_id(current_struct[2]) in closed_list:
                continue;
            closed_list[self.prob.get_node_id(current_struct[2])] = \
                    [current_struct[3], current_struct[4]]
            if current_struct[2] in self.prob.goals:
                break;
            successors = self.prob.get_successors(current_struct[2])
            for successor in successors:
                if self.prob.get_node_id(successor[0]) in closed_list:
                    continue;
                cost = current_struct[1] + successor[1]
                f = self.get_heuristic(successor[0]) + cost
                open_list.put([f, cost, successor[0], successor[2], current_struct[2]])
            # crap = input('wait')
        plan = [current_struct[2]] + plan
        parent = [current_struct[3], current_struct[4]]
        while parent[1] != -1:
            plan = parent + plan
            parent = closed_list[self.prob.get_node_id(parent[1])]
        return (plan, cost)

    def get_heuristic(self, node):
        return 0
