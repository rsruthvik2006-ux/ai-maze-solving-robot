*Purpose: Implements core pathfinding logic (using Breadth-First Search / A*) to navigate grid spaces.*

```python
from collections import deque

class MazeSolver:
    def __init__(self, grid_size=(10, 10)):
        self.grid_size = grid_size
        self.visited = set()

    def bfs_pathfind(self, start, goal, obstacles):
        """Finds the shortest path using Breadth-First Search."""
        queue = deque([[start]])
        visited = set([start])

        while queue:
            path = queue.popleft()
            current = path[-1]

            if current == goal:
                return path

            # Explore neighbors (Up, Down, Left, Right)
            neighbors = [
                (current[0] + 1, current[1]),
                (current[0] - 1, current[1]),
                (current[0], current[1] + 1),
                (current[0], current[1] - 1)
            ]

            for neighbor in neighbors:
                if (0 <= neighbor[0] < self.grid_size[0] and
                    0 <= neighbor[1] < self.grid_size[1] and
                    neighbor not in obstacles and
                    neighbor not in visited):
                    
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    
        return None
