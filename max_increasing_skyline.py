import unittest

def maxIncreaseKeepingSkyline(grid) -> int:
    # get max height allowed for each row in the grid
    max_row_heights = [max(row) for row in grid]
    
    #get max height allowed for each column in the grid
    cols = []
    for i in range(len(grid[0])):
        cols.append([row[i] for row in grid])
    max_col_heights = [max(col) for col in cols]

    total_increase = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # total allowed height increase is the minimum of the max increase for a given row and column
            total_increase += min(max_row_heights[i], max_col_heights[j]) - grid[i][j]
    return total_increase

class SkylineTest(unittest.TestCase):
    def test(self):
        test_grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
        self.assertEqual(maxIncreaseKeepingSkyline(test_grid), 35)

if __name__ == '__main__':
    unittest.main()