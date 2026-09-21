# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = []
        d = {}
        curr = head
        while curr:
            if curr.val in d:
                d[curr.val] += 1
            else:
                d[curr.val] = 1
            curr = curr.next

        for key, data in d.items():
            if data >=2:
                continue
            res.append(key)

        res.sort()
        
        dummy = ListNode(0)
        curr = dummy

        for value in res:
            curr.next = ListNode(value)
            curr = curr.next
        return dummy.next
        


        

        