class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        dummy = ListNode()
        dummy.next = slow
        return dummy.next
        

if __name__ == "__main__":
    s = Solution()

    node1 = ListNode(1)    
    node2 = ListNode(2)
    node2.next = node1
    node3 = ListNode(3)
    node2.next = node3
    node4 = ListNode(4)
    node3.next = node4
    node5 = ListNode(5)
    node4.next = node5
    
    print(s.hasCycle(node1))


