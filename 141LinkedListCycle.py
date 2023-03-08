class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, headListNode) -> bool:
        slow, fast = headListNode, headListNode

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    node1 = ListNode(3)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(0)
    node2.next = node3
    node4 = ListNode(-4)
    node3.next = node4
    node4.next = node2