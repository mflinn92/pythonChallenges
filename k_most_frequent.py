import unittest
#Given a non-empty array of integers, return the k most frequent elements.

def top_k_frequent_initial(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if k > len(nums):
        return -1
    frequencies = {}
    for num in nums:
        frequencies[num] = frequencies.get(num, 0) + 1
    sorted_by_freq = sorted(frequencies.items(), key= lambda val: val[1])
    output = []
    n = len(sorted_by_freq) - 1
    while len(output) < k:
        output.append(sorted_by_freq[n][0])
        n -= 1
    return output

def top_k_frequent_bucket_sort(nums ,k):
    frequencies = {}
    for num in nums:
        frequencies[num] = frequencies.get(num, 0) + 1
    freq_buckets = [None] * (len(nums) + 1)

    for num, freq in frequencies.items():
        if not freq_buckets[freq]:
            freq_buckets[freq] = [num]
        else:
            freq_buckets[freq].append(num)
    result = []
    for val in reversed(freq_buckets):
        if val:
            result += val
        if len(result) == k:
            break
    return result



class Test(unittest.TestCase):
    def test_most_frequent(self):
        test_list = [1,1,1,2,2,3]
        self.assertEqual(top_k_frequent_initial(test_list, 2), [1,2])

    def test_invalid_k(self):
        test_list = [2,3,4,2]
        self.assertEqual(top_k_frequent_initial(test_list, 7), -1)
    
    def test_bucket_method(self):
        test_list = [1,1,1,2,2,3]
        self.assertEqual(top_k_frequent_bucket_sort(test_list, 2), [1,2])

if __name__ == '__main__':
    unittest.main()


