# https://leetcode.com/problems/number-of-islands/description
#
#
#
#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from typing import List

def solution(grid: List[List[str]]) -> int:
    
    number_island = 0
    
    m = len(grid)
    n = len(grid[0])
    for row in range(m):
        for column in range(n):
            if grid[row][column] == "1":
                island_queue = []
                number_island += 1
                island_queue.append((row, column))
                grid[row][column] = "0"
                
                while island_queue:
                    r, c = island_queue.pop(0)
                    
                    if r-1 >= 0 and grid[r-1][c] == "1":
                        island_queue.append((r-1, c))
                        grid[r-1][c] = "0"
                    if r+1 < m and grid[r+1][c] == "1":
                        island_queue.append((r+1, c))
                        grid[r+1][c] = "0"
                    if c-1>=0 and grid[r][c-1] == "1":
                        island_queue.append((r, c-1))
                        grid[r][c-1] = "0"
                    if c+1 < n and grid[r][c+1] == "1":
                        island_queue.append((r, c+1))
                        grid[r][c+1] = "0"
            
    return number_island
