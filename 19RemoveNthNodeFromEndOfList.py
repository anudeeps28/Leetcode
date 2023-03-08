from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head
       
        while n > 0 and right:
           right = right.next
           n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next
        
        



        

if __name__ == "__main__":
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3
    node4 = ListNode(4)
    node3.next = node4
    node5 = ListNode(5)
    node4.next = node5

    s.removeNthFromEnd(node1, 4)