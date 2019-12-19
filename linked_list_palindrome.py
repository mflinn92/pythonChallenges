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

    def isPalindrome(self):
        # O(n) time O(n) space solution
        curr_node = self.head
        node_vals = []
        while curr_node:
            node_vals.append(curr_node.val)
            curr_node = curr_node.next
        return node_vals == node_vals[::-1]

    def isPalindrome_space_efficient(self):
        # O(n) time O(1) space
        list_length = 0
        curr_node = self.head
        # determine length of list
        while curr_node:
            list_length += 1
            curr_node = curr_node.next
            
        mid_idx = list_length // 2
        # set variables used for reversing the first half of list
        list_index = 0
        prev = None
        curr_node = self.head
        #reverse first half of list
        while list_index < mid_idx:
            temp = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = temp
            list_index += 1
            
        first_half = prev
        # if list is of odd length we can ignore the middle most node
        if (list_length % 2 == 1):
            curr_node = curr_node.next
        while curr_node and first_half:
            if curr_node.val != first_half.val:
                return False
            curr_node = curr_node.next
            first_half = first_half.next
        return True

class Test(unittest.TestCase):
    def test_is_palindrome(self):
        test_list = LinkedList()
        for i in range(10000):
            test_list.prepend(i)
        for i in reversed(range(10000)):
            test_list.prepend(i)
        self.assertEqual(test_list.isPalindrome(), True)
        self.assertEqual(test_list.isPalindrome_space_efficient(), True)
    
    def test_is_not_palindrome(self):
        test_list = LinkedList()
        for i in range(10000):
            test_list.prepend(i)
        self.assertEqual(test_list.isPalindrome(), False)
        self.assertEqual(test_list.isPalindrome_space_efficient(), False)


if __name__ == '__main__':
    unittest.main()