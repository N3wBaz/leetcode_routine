class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        current = head
        while current and current.next:
            if current.val == current.next.val:
                # Пропускаем следующий узел, так как он дублируется
                current.next = current.next.next
            else:
                # Переходим к следующему узлу
                current = current.next

        return head