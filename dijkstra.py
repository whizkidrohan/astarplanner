from Queue import PriorityQueue
class Dijstra:

    # problem = object of problem class
    def __init__(self, problem):
        self.prob = problem

    # returns the optimal cost from every node to goal
    def get_cost(self):
        start_node = self.prob.start
        plan = []
        cost_star = [[-1 for i in range(self.prob.size[0])] \
                for j in range(self.prob.size[1])]
        # struct = [f, cost, node, action, parent]
        open_list = PriorityQueue()
        open_list_g = {}
        closed_list = {}

        # initialize open list with all goals
        for goal in self.prob.goals:
            cost = self.prob.cost[goal[0]][goal[1]]
            goal_id = self.prob.get_node_id(goal)
            open_list.put([cost, cost, goal, -1, -1])
            open_list_g[goal_id] = cost
        counter = 0
        while not open_list.empty():
            # for l in open_list.queue:
                # print l
            current_struct = open_list.get()
            # for cs in cost_star:
                # print cs
            # print current_struct
            if cost_star[current_struct[2][0]][current_struct[2][1]] != -1:
                continue;
            cost_star[current_struct[2][0]][current_struct[2][1]] = current_struct[1]
            successors = self.prob.get_successors(current_struct[2])
            for successor in successors:
                successor_id = self.prob.get_node_id(successor[0])
                if cost_star[successor[0][0]][successor[0][1]] != -1:
                    continue;
                successor_cost = current_struct[1] + successor[1]
                if successor_id in open_list_g:
                    if open_list_g[successor_id] <= successor_cost:
                        continue;
                open_list.put([successor_cost, successor_cost, successor[0], successor[2], current_struct[2]])
            # crap = input('wait')
            counter = counter + 1
            # print counter
        return cost_star
