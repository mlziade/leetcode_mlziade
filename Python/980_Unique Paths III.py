from typing import List

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nodes = list()

class Solution:
    
    m = 0
    n = 0
    start = [0,0]
    walls = set()
    end = [0,0]
    total_blocks_to_walk = 0
    node = None

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.find_relevant_quares(grid)
        self.currentPath = []
        self.node = Node(self.start[0], self.start[1])
        return self.find_unique_path(grid, self.start[0], self.start[1], self.node, [])
    
    def find_relevant_quares(self, grid):
        self.m = len(grid)
        self.n = len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.start = [i, j]
                elif grid[i][j] == 2:
                    self.end = [i, j]
                elif grid[i][j] == -1:
                    self.walls.add((i, j))
                else:
                    self.total_blocks_to_walk += 1

    def find_unique_path(self, grid, x, y, node, path):
        if (x, y) == (self.end[0], self.end[1]):
            if len(path) == self.total_blocks_to_walk + 1:
                return 1
            return 0
        
        path.append((x, y))
        total_paths = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.m and 0 <= ny < self.n and (nx, ny) not in path and (nx, ny) not in self.walls:
                total_paths += self.find_unique_path(grid, nx, ny, node, path)
        path.pop()
        return total_paths

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))


