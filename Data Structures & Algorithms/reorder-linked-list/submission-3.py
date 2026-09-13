# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        # step 1 : To identify the mid point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # step 2 : To reverse the second half

        curr, prev = slow.next, None
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # step 3 : Merge two linked list now

        first, second = head, prev

        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next, second.next = second, tmp1
            first, second = tmp1, tmp2
        




        
        