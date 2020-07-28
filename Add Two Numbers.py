# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        head = result
        carry = 0
        while l1 or l2: 
            if l1: 
                num1 = l1.val
                l1 = l1.next
            else: 
                num1 = 0    
            if l2:
                num2 = l2.val
                l2 = l2.next
            else: 
                num_2 = 0
            num3 = num1 + num2 + carry
            if num3 > 9 : 
                result.next = ListNode(num3 % 10)
                carry = 1
            else: 
                result.next = ListNode(num3)
                carry = 0
            result = result.next
        if carry == 1: 
            result.next = ListNode(carry)
        return head.next