# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        first = None
        last = None
        while l1 or l2 or carry == 1:
            num1 = 0
            num2 = 0

            if l1:
                num1 = l1.val
                l1 = l1.next
            
            if l2:
                num2 = l2.val
                l2 = l2.next

            sum = num1 + num2 + carry
            carry = sum / 10
            digit = sum % 10
            
            if not first:
                last = ListNode(digit)
                first = last
            else:
                last.next = ListNode(digit)
                last = last.next
        
        return first