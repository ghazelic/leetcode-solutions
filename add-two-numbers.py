# Essentially, iterate through both linked lists, while adding the current digit
# loop will iterate until the end of the largest linked list, but also if there is a carry over value
# the carry over value is defined before hand, and is a condition for the while loop
# was caught up on defining the linked list, i now know that you can set a head, and a pointer for traversal.

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

        # create two nodes, one a pointer, one the head. Return the NEXT value of the head, but first set the next value of the head to NONE
        tempHead = ListNode(0)
        tail = tempHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            # better syntax for setting the value of something
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0
            

            sum = digit1 + digit2 + carry
            digit = sum % 10 
            carry = sum // 10

            # create new node
            newNode = ListNode(digit)

            # set the pointer next to new node
            tail.next = newNode

            # advance pointer
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        result = tempHead.next

        # remove the temp head with node value of 0
        tempHead.next = None
        return result
            

            
