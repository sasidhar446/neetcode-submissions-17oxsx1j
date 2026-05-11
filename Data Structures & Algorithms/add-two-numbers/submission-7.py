# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2, carry = l1, l2, 0
        dummy = ListNode()
        tail = dummy

        while curr1 and curr2:
            total = curr1.val + curr2.val + carry
            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next
            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1:
            total = curr1.val + carry
            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next
            curr1 = curr1.next

        
        while curr2:
            total = curr2.val + carry
            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next
            curr2 = curr2.next
        
        if carry > 0:
            tail.next = ListNode(carry)

        
        return dummy.next

