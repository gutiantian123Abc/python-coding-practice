"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        l3 = ListNode(0)
        dummy = l3

        while l1 and l2:
            val_1, val_2 = l1.val, l2.val
            sum = val_1 + val_2 + carry
            digit = sum % 10
            carry = sum // 10

            """
            /  = exact division result
            // = floor division result
            | Expression  | Meaning         | Result |
            | ----------- | --------------- | ------ |
            | `18 / 10`   | normal division | `1.8`  |
            | `18 // 10`  | floor division  | `1`    |
            | `25 / 5`    | normal division | `5.0`  |
            | `25 // 5`   | floor division  | `5`    |
            | `25.5 / 5`  | normal division | `5.1`  |
            | `25.5 // 5` | floor division  | `5.0`  |
            """

            l3.next = ListNode(digit)
            l3 = l3.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val
            sum = val + carry
            digit = sum % 10
            carry = sum // 10
            l3.next = ListNode(digit)
            l3 = l3.next
            l1 = l1.next

        while l2:
            val = l2.val
            sum = val + carry
            digit = sum % 10
            carry = sum // 10
            l3.next = ListNode(digit)
            l3 = l3.next
            l2 = l2.next

        if carry != 0:
            l3.next = ListNode(carry)
            l3 = l3.next

        return dummy.next
