# pathfinder/agent.py

import heapq
import time

# Heuristic function
def manhattan_distance(pos1, pos2):
    """Calculates the Manhattan distance between two points."""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

class Agent:
    """
    The autonomous agent that navigates the grid world.
    Contains implementations of pathfinding algorithms.
    """
    def __init__(self, environment):
        self.env = environment
        self.path = []
        self.nodes_expanded = 0
        self.execution_time = 0
        self.total_cost = 0

    def _reconstruct_path(self, came_from, current):
        """Reconstructs the path from the goal back to the start."""
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1] # Reverse the path to get start -> goal

    def uniform_cost_search(self):
        """
        Uniform-Cost Search (UCS) algorithm.
        Finds the cheapest path from start to goal.
        """
        start_time = time.time()
        priority_queue = [(0, self.env.start)]
        came_from = {}
        cost_so_far = {self.env.start: 0}
        self.nodes_expanded = 0

        while priority_queue:
            current_cost, current_pos = heapq.heappop(priority_queue)
            self.nodes_expanded += 1

            if current_pos == self.env.goal:
                self.path = self._reconstruct_path(came_from, current_pos)
                self.total_cost = cost_so_far[current_pos]
                self.execution_time = time.time() - start_time
                return self.path

            for neighbor in self.env.get_neighbors(current_pos):
                # First, check if the neighbor is a valid spot on the map.
                if self.env.is_valid(neighbor):
                    move_cost = self.env.get_cost(neighbor)
                    new_cost = cost_so_far[current_pos] + move_cost
                    
                    if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                        cost_so_far[neighbor] = new_cost
                        priority = new_cost
                        heapq.heappush(priority_queue, (priority, neighbor))
                        came_from[neighbor] = current_pos
        
        self.execution_time = time.time() - start_time
        return None # Path not found

    def a_star_search(self, heuristic_func):
        """
        A* Search algorithm.
        Uses a heuristic to find the cheapest path more efficiently.
        """
        start_time = time.time()
        priority_queue = [(0, self.env.start)]
        came_from = {}
        cost_so_far = {self.env.start: 0}
        self.nodes_expanded = 0

        while priority_queue:
            _, current_pos = heapq.heappop(priority_queue)
            self.nodes_expanded += 1
            
            if current_pos == self.env.goal:
                self.path = self._reconstruct_path(came_from, current_pos)
                self.total_cost = cost_so_far[current_pos]
                self.execution_time = time.time() - start_time
                return self.path
            
            current_time_step = len(self._reconstruct_path(came_from, current_pos))

            for neighbor in self.env.get_neighbors(current_pos):
                # First, check if the neighbor is a valid spot at the next time step.
                if self.env.is_valid(neighbor, current_time_step + 1):
                    move_cost = self.env.get_cost(neighbor)
                    new_cost = cost_so_far[current_pos] + move_cost

                    if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                        cost_so_far[neighbor] = new_cost
                        priority = new_cost + heuristic_func(neighbor, self.env.goal)
                        heapq.heappush(priority_queue, (priority, neighbor))
                        came_from[neighbor] = current_pos

        self.execution_time = time.time() - start_time
        return None # Path not found