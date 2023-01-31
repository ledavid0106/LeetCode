# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodeList = []
        while head!=None:
            nodeList.append(head)
            head = head.next
        return nodeList[len(nodeList)//2]