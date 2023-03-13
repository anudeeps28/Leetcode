class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        temp = node.next
        node.val = node.next.val
        node.next = node.next.next
        temp.next = None


        

if __name__ == "__main__":
    s = Solution()

    node4 = ListNode(4)
    node5 = ListNode(5)
    node4.next = node5
    node1 = ListNode(1)
    node5.next = node1
    node9 = ListNode(9)
    node1.next = node9

    s.deleteNode(node5)
