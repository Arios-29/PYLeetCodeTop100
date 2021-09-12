from queue import PriorityQueue
from typing import List


class ListNode:
    def __init__(self, val=0, right=None):
        self.val = val
        self.right = right


class NodeComparable:
    def __init__(self, node: ListNode):
        self.node = node

    def __cmp__(self, other):
        return self.node.val - other.node.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        queue = PriorityQueue()
        for node in lists:
            if node is not None:
                queue.put(NodeComparable(node))
        head = ListNode()
        pre = head
        while not queue.empty():
            minNode = queue.get().node
            pre.right = minNode
            pre = pre.right
            if minNode.right is not None:
                nextNode = NodeComparable(minNode.right)
                queue.put(nextNode)
        return head.right
