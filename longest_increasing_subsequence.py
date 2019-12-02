import unittest

# Given an unsorted array of integers, find the length of longest increasing subsequence.

def longest_increasing_sub(nums) -> int:
    if not nums:
        return 0
    increasing_length_dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                increasing_length_dp[i] = max(increasing_length_dp[i], increasing_length_dp[j] + 1)
    return max(increasing_length_dp)


class TestCases(unittest.TestCase):
    def test_simple(self):
        test_list = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(longest_increasing_sub(test_list), 4)

    def test_empty_list(self):
        test_list = []
        self.assertEqual(longest_increasing_sub(test_list), 0)
    
    def test_complex(self):
        test_list = [4, 10, 4, 3, 8, 9]
        self.assertEqual(longest_increasing_sub(test_list), 3)

if __name__ == '__main__':
    unittest.main() 