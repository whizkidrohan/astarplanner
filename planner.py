from Queue import PriorityQueue
class Planner:
    # Gives a plan from start to goal

    # heuristic = an array with size of space
    # problem = object of problem class
    def __init__(self, problem, heuristic):
        self.prob = problem
        self.heuristic = heuristic

    def get_path(self):
        w=1
        start_node = self.prob.start
        plan = []
        cost = -1
        # struct = [f, cost, node, action, parent]
        open_list = PriorityQueue()
        open_list_f = {}
        # closed_list = [node] -> [action, parent, cost]
        closed_list = {}
        cost = self.prob.cost[start_node[0]][start_node[1]]
        f = cost+ w*self.get_heuristic(start_node)
        open_list.put([f, cost, start_node, -1, -1])
        open_list_f[self.prob.get_node_id(start_node)]=f;

        while open_list:
            # print "Open List"
            # for l in open_list.queue:
                # print l
            current_struct = open_list.get()
            if self.prob.get_node_id(current_struct[2]) in closed_list:
                continue;
            closed_list[self.prob.get_node_id(current_struct[2])] = \
                    [current_struct[3], current_struct[4], current_struct[1]]
            if current_struct[2] in self.prob.goals:
                break;
            successors = self.prob.get_successors(current_struct[2])
            for successor in successors:
                successor_id = self.prob.get_node_id(successor[0])
                if successor_id in closed_list:
                    continue;
                cost = current_struct[1] + successor[1]
                f = w*self.get_heuristic(successor[0]) + cost
                if successor_id in open_list_f:
                    if open_list_f[successor_id] <= f:
                        continue;
                open_list.put([f, cost, successor[0], successor[2], current_struct[2]])
            # crap = input('wait')
        current_state = [current_struct[3], current_struct[2], current_struct[1]]
        parent = closed_list[self.prob.get_node_id(current_struct[2])]
        while parent[1] != -1:
            plan = [current_state[0:2]] + plan
            current_state = parent
            parent = closed_list[self.prob.get_node_id(parent[1])]
            cost = parent[2]
        plan = [current_state[0:2]] + plan
        return plan

    def get_heuristic(self, node):
        return self.heuristic[node[0]][node[1]]
