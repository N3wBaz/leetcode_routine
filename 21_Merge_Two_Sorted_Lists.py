# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        current = dummy  # Pointer to build the merged list
        
        # Traverse both lists and merge nodes in sorted order
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Move the pointer forward
        
        # If one of the lists is not empty, append it to the result
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the merged list, starting from the node after dummy
        return dummy.next