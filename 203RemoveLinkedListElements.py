class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        currentNode = dummyHead
        
        while currentNode.next != None:
            if currentNode.next.val == val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
                
        return dummyHead.next

       
