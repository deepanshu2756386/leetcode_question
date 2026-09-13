# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = ListNode(-1)
        ans.next = head
        curr = ans

        while curr.next !=None and curr.next.next !=None:
            first = curr.next 
            second = curr.next.next

            first.next = second.next
            second.next = first 
            curr.next = second 

            curr = first 

        return ans.next 
        
        