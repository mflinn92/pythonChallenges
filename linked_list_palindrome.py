import unittest

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self, value):
        node = ListNode(value)
        if self.head: 
            node.next = self.head
        self.head = node


def isPalindrome(head):
        # O(n) time O(n) space solution
    node_vals = []
    while head:
        node_vals.append(head.val)
        head = head.next
    return node_vals == node_vals[::-1]

class Test(unittest.TestCase):
    def test_is_palindrome(self):
        test_list = LinkedList()
        test_list.prepend(1)
        test_list.prepend(0)
        test_list.prepend(1)
        self.assertEqual(isPalindrome(test_list.head), True)
    
    def test_is_not_palindrome(self):
        test_list = LinkedList()
        for i in range(10):
            test_list.prepend(i)
        self.assertEqual(isPalindrome(test_list.head), False)


if __name__ == '__main__':
    unittest.main()