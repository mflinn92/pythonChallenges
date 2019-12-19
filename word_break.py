import unittest
from collections import deque


def word_break(s, word_dict):
    word_hash = set(word_dict)
    queue = deque([0])
    visited = set()
    while queue:
        start_idx = queue.popleft()
        if start_idx not in visited:
            for end in range(start_idx + 1, len(s) + 1):
                if s[start_idx:end] in word_hash:
                    queue.append(end)
                    if end == len(s):
                        return True
        visited.add(start_idx)
    return False

class Test(unittest.TestCase):
    def test_basic(self):
        test_str = 'catsdogs'
        word_list = ['cats', 'dogs']
        self.assertEqual(word_break(test_str, word_list), True)

    def test_not_breakable(self):
        test_str = 'catsandogs'
        word_list = ['cat', 'cats', 'sand', 'dogs']
        self.assertEqual(word_break(test_str, word_list), False)

if __name__ == '__main__':
    unittest.main()