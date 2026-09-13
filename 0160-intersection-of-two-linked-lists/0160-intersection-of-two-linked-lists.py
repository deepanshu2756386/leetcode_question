# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        
        c = 0

        while True:

            if p1 == p2:
                return p1 


            if p2 == None:
                c += 1
                p2 = headA

            else:
                p2 = p2.next

            if p1 == None:
                p1 = headB

            else:
                p1 = p1.next 

            if c>1:
                return None



        