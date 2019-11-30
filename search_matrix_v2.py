import unittest

def search_matrix(matrix, target):
    #perform binary search on rows to determine which row target val should be in. 
    if not matrix or not matrix[0]:
        return False
    target_row = bsearch_rows(matrix, target)
    # binary search the row that should contain target
    return bsearch(matrix[target_row], target)

def bsearch_rows(grid, target):
    if len(grid) == 1:
        return 0
    start = 0
    end = len(grid) - 1
    while start < end:
        mid_row = (start + end) // 2
        if grid[mid_row][0] <= target and grid[mid_row + 1][0] > target:
            return mid_row
        if target < grid[mid_row][0]:
            end = mid_row - 1
        else:
            start = mid_row + 1
    return start
        
   
def bsearch(row, target):
    start = 0
    end = len(row) - 1
    while start <= end:
        mid = (start + end) // 2
        if row[mid] == target:
            return True
        if target < row[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


class SearchTest(unittest.TestCase):
    def test_row_search(self):
        test_grid = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        self.assertEqual(bsearch_rows(test_grid, 7), 2)

    def test_bsearch(self):
        test_list = [1,2,3,4,5,7]
        self.assertEqual(bsearch(test_list, 2), True)
    
    def test_search(self):
        test_grid = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        self.assertEqual(search_matrix(test_grid, 16), True)
        self.assertEqual(search_matrix(test_grid, 21), False)
    def test_empty_grid(self):
        test_grid = []
        self.assertEqual(search_matrix(test_grid, 3), False)

if __name__ == '__main__':
    unittest.main()