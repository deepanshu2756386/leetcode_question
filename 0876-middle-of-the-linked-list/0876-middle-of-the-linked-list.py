# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # curr = head
        # l = 0 
        # while curr != None:
        #     curr = curr.next
        #     l +=1

        # curr = head 

        # for i in  range(l//2):
        #     curr = curr.next

        # return curr

        slow = head
        fast = head
        while fast !=None and fast.next !=None:
            slow = slow.next
            fast = fast.next.next

        return slow

        