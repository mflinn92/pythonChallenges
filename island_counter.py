import unittest


def islandCounter(grid):
    #iterate through grid until island is found
    num_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                num_islands += 1
                #used for dfs of adjacent land
                stack = [(i, j)]
                while stack:
                    curr_row, curr_col = stack.pop()
                    grid[curr_row][curr_col] = "0"
                    #check up
                    if curr_row > 0 and grid[curr_row -1][curr_col] == "1":
                        stack.append((curr_row-1, curr_col))
                    #check down
                    if curr_row < (len(grid) - 1) and grid[curr_row + 1][curr_col] == "1":
                        stack.append((curr_row + 1, curr_col))
                    #check left
                    if curr_col > 0 and grid[curr_row][curr_col - 1] == "1":
                        stack.append((curr_row, curr_col - 1))
                    #check right
                    if curr_col < (len(grid[0]) - 1) and grid[curr_row][curr_col + 1] == "1":
                        stack.append((curr_row, curr_col + 1))
    return num_islands

class TestIslandCount(unittest.TestCase):
    def test_single_island(self):
        test_grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]
        self.assertEqual(islandCounter(test_grid), 1)
    
    def test_no_islands(self):
        test_grid = [
            ["0","0"],
            ["0","0"]]
        self.assertEqual(islandCounter(test_grid), 0)
    def test_multiple_islands(self):
        test_grid = [
            ["0", "0", "1", "0"],
            ["1", "1", "0", "0"],
            ["1", "0", "0", "1"],
            ["0", "1", "0", "1"]]
        self.assertEqual(islandCounter(test_grid), 4)
if __name__ == '__main__':
    unittest.main()

