# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        
        l1Pointer = l1
        l2Pointer = l2

        totalSum = 0
        currentMultiplier = 1

        # sum the two values
        while l1Pointer:
            totalSum += l1Pointer.val * currentMultiplier
            currentMultiplier *= 10
            l1Pointer = l1Pointer.next
        
        currentMultiplier = 1
        while l2Pointer:
            totalSum += l2Pointer.val * currentMultiplier
            currentMultiplier *= 10
            l2Pointer = l2Pointer.next
            

        pointer = ListNode()
        head = pointer
        if totalSum == 0:
            return head
        currentRemainder = totalSum

        while currentRemainder != 0:
            pointer.next = ListNode(currentRemainder % 10)
            currentRemainder = currentRemainder // 10
            pointer = pointer.next

        return head.next
