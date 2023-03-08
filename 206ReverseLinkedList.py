# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        previous = None
        current = head
        
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous

            

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

    s.reverseList(node1)