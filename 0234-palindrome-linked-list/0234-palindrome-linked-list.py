# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
                    return None

        tempStack = []
        temp = head
        while temp:
            tempStack.append(temp.val)
            temp = temp.next

        while head:
            if head.val != tempStack.pop():
                return False
            head = head.next

        return True