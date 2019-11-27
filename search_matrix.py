import unittest
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

def search_matrix(matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    # start from top right corner
    curr_row, curr_col = 0, len(matrix[0]) - 1
    while (curr_row < len(matrix) and curr_col >= 0):
        
        if target == matrix[curr_row][curr_col]:
            return True
        # eliminate last column form search space if current value larger than target
        if target < matrix[curr_row][curr_col]:   
            curr_col -= 1
            # eliminate top row from search if current value < target
        if target > matrix[curr_row][curr_col]:
            curr_row += 1
    return False 
    
class SearchTest (unittest.TestCase):
    def test_value_present(self):
        test_grid = [
            [1,4,7,11,15],
            [2,5,8,12,19],
            [3,6,9,16,22],
            [10,13,14,17,24],
            [18,21,23,26,30]
        ]
        self.assertEqual(search_matrix(test_grid, 14), True)
    def test_value_not_present(self):
        test_grid = [
            [1,4,7,11,15],
            [2,5,8,12,19],
            [3,6,9,16,22],
            [10,13,14,17,24],
            [18,21,23,26,30]
        ]
    def test_empty_grid(self):
        test_grid = []
        self.assertEqual(search_matrix(test_grid, 23), False)

    def test_empty_rows(self):
        test_grid = [[], [], []]
        self.assertEqual(search_matrix(test_grid, 6), False)
        
if __name__ == "__main__":
    unittest.main()