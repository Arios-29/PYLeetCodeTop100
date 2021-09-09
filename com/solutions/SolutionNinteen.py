class ListNode:
    def __init__(self, val=0, right=None):
        self.val = val
        self.right = right


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(-1, head)
        cur = head
        end = head
        i = 1
        while i < n:
            end = end.right
            i += 1
        while end.right is not None:
            pre = pre.right
            cur = cur.right
            end = end.right
        if cur == head:
            return head.right
        else:
            pre.right = cur.right
            return head
