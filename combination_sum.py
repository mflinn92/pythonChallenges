import unittest

def combination_sum(candidates, target):
    if not candidates:
        return -1
    output = backtrack(candidates, target, [], [])
    return output

def backtrack(candidates, target, proposal, result):
    if target == 0:
        result.append(proposal.copy())
        return result
    elif target < 0:
        return result
    else: 
        for i, num in enumerate(candidates):
            backtrack(candidates[i:], target - num, proposal + [num], result)
        return result

class Test(unittest.TestCase):
    def test_simple_case(self):
        candidates = [2,3,6,7]
        target = 7
        expected = [
            [2,2,3],
            [7]
        ]
        self.assertEqual(combination_sum(candidates, target), expected)

if __name__ == '__main__':
    unittest.main()