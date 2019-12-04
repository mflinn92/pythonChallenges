import unittest
'''
You are given a map in form of a two-dimensional 
integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island 
(i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
'''

def island_perimeter(grid):
    edge_count = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):          
            if col == 1:
                edge_count += 4
                if i > 0 and grid[i-1][j]:
                    edge_count -= 1
                if j > 0 and grid[i][j-1]:
                    edge_count -= 1
                if i < len(grid) - 1 and grid[i+1][j]:
                    edge_count -= 1
                if j < len(row) and grid[i][j+1]:
                    edge_count -=1 
    return edge_count

class Test(unittest.TestCase):
    def test(self):
        test_grid = [
            [0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]
        ]
        self.assertEqual(island_perimeter(test_grid), 16)
    
    def test_no_island(self):
        test_grid = [[]]
        self.assertEqual(island_perimeter(test_grid), 0)

if __name__ == '__main__':
    unittest.main()