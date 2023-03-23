from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # save ptrs
            second = curr.next
            nextPair = curr.next.next
            

            # reverse this pair
            second.next = curr
            curr.next = nextPair
            prev.next = second

            # update ptrs
            prev = curr
            curr = nextPair
        
        return dummy.next



if __name__ == "__main__":
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    s.swapPairs(node1)