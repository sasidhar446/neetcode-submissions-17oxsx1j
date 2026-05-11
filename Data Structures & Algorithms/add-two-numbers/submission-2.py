# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, num: int) -> int:
        rev = 0
        while num > 0:
            rem = num % 10
            num = num // 10
            rev = rev * 10 + rem
        return rev
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr1, num1 = l1, ""
        while curr1:
            num1 += str(curr1.val)
            curr1 = curr1.next
        
        curr2, num2 = l2, ""
        while curr2:
            num2 += str(curr2.val)
            curr2 = curr2.next

        num1 = self.reverse(int(num1))
        num2 = self.reverse(int(num2))

        total = str(num1 + num2)

        dummy = ListNode()
        tail = dummy

        for i in range(len(total) - 1, -1, -1):
            tail.next = ListNode(total[i])
            tail = tail.next
        
        return dummy.next






