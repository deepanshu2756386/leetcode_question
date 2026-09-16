# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        slow = head
        fast = head

        while fast !=None and fast.next !=None:
            slow = slow.next
            fast = fast.next.next  

        curr = slow
        prev = None
        nxt = None 

        while curr !=None :
            nxt = curr.next 
            curr.next = prev
            prev = curr 
            curr  = nxt

        first = head 
        second =prev 
        while second !=None:
            if first.val !=second.val :
                return False

            first = first.next 
            second  = second.next 

        return True 


        