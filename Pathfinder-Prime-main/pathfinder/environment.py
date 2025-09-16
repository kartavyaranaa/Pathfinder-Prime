# pathfinder/environment.py

import time

class GridWorld:
    """
    Represents the 2D grid city environment.
    Handles loading maps, defining costs, and managing obstacles.
    """
    def __init__(self, map_filepath):
        self.grid = []
        self.costs = {}
        self.start = None
        self.goal = None
        self.width = 0
        self.height = 0
        self.dynamic_obstacles = {} # Stores positions of moving obstacles at each time step
        self._load_map(map_filepath)
        self._define_costs()

    def _load_map(self, filepath):
        """Loads a map from a text file."""
        with open(filepath, 'r') as f:
            for y, line in enumerate(f):
                row = list(line.strip())
                if 'S' in row:
                    self.start = (row.index('S'), y)
                if 'G' in row:
                    self.goal = (row.index('G'), y)
                self.grid.append(row)
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def _define_costs(self):
        """Defines the movement cost for different terrain types."""
        self.costs = {
            '.': 1,  # Normal
            'T': 3,  # Tough
            'W': 5,  # Water
            'S': 1,  # Start is on normal ground
            'G': 1   # Goal is on normal ground
        }

    def get_cost(self, position):
        """Gets the movement cost of a cell."""
        x, y = position
        char = self.grid[y][x]
        return self.costs.get(char, float('inf')) # Walls '#' will have infinite cost

    def is_valid(self, position, time_step=0):
        """Checks if a position is within bounds, not a static obstacle,
           and not occupied by a dynamic obstacle at a given time."""
        x, y = position
        # Check bounds
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False
        # Check static obstacles
        if self.grid[y][x] == '#':
            return False
        # Check dynamic obstacles for the given time step
        if self.dynamic_obstacles.get(time_step) and position in self.dynamic_obstacles[time_step]:
            return False
        return True

    def get_neighbors(self, position):
        """Gets the 4-connected neighbors of a position."""
        x, y = position
        neighbors = []
        # Up, Down, Left, Right
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_x, new_y = x + dx, y + dy
            neighbors.append((new_x, new_y))
        return neighbors
        
    def add_dynamic_obstacle_schedule(self, schedule):
        """
        Adds a schedule for dynamic obstacles.
        Format: {time_step: [(x1, y1), (x2, y2)], ...}
        """
        self.dynamic_obstacles = schedule

    def visualize_path(self, path):
        """Prints the grid with the calculated path."""
        grid_copy = [list(row) for row in self.grid]
        for pos in path:
            if pos != self.start and pos != self.goal:
                grid_copy[pos[1]][pos[0]] = '*'
        for row in grid_copy:
            print(" ".join(row))