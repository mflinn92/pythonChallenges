import unittest

def subarray_sum(nums, target):
    current_sum = 0
    result = 0
    map = {}
    map[0] = 1
    for num in nums:
        current_sum += num
        if current_sum - target in map:
            result += map[current_sum - target]
        map[current_sum] = map.get(current_sum, 0) + 1
    return result

class SubarraySumTest(unittest.TestCase):
    def basic_test(self):
        test_list = [1,1,1]
        self.assertEqual(subarray_sum(test_list, 2), 2)

    def empty_test(self):
        test_list = []
        self.assertEqual(subarray_sum(test_list, 0), 0)
    
    def test(self):
        test_list = [1, 4, -2, 3, 5, 2]
        self.assertEqual(subarray_sum(test_list, 3), 2)

if __name__ == '__main__':
    unittest.main()