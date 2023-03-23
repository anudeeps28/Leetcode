from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            # update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
        



if __name__ == "__main__":
    s = Solution()
    node2 = ListNode(2)
    node4 = ListNode(4)
    node3 = ListNode(3)
    node2.next = node4
    node4.next = node3

    node5 = ListNode(5)
    node6 = ListNode(6)
    node24 = ListNode(4)
    node5.next = node6
    node6.next = node24

    s.addTwoNumbers(node2, node5)