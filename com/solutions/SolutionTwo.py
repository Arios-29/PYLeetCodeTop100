class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionTwo:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        cur = head
        tmp = 0
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + tmp
            if sum >=10:
                sum=sum-10
                tmp=1
            else:
                tmp=0
            node = ListNode(sum)
            cur.next=node
            cur=cur.next
            l1=l1.next
            l2=l2.next
        while l1 is not None:
            sum = l1.val + tmp
            if sum >=10:
                sum=sum-10
                tmp=1
            else:
                tmp=0
            node = ListNode(sum)
            cur.next=node
            cur=cur.next
            l1=l1.next
        while l2 is not None:
            sum = l2.val+tmp
            if sum>=10:
                sum=sum-10
                tmp=1
            else:
                tmp=0
            node = ListNode(sum)
            cur.next=node
            cur=cur.next
            l2=l2.next
        if tmp==1:
            node = ListNode(1)
            cur.next=node
        return head.next

