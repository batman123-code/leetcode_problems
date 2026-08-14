
# 82. Remove Duplicates from Sorted List II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         dummy=ListNode(0)
#         curr=head
#         prev=dummy
#         dummy.next=head
#         while curr:
#             if(curr.next and curr.val==curr.next.val):
#                 duplicate=curr.val
#                 while(curr and curr.val==duplicate):
#                     curr=curr.next
#                 prev.next=curr
#             else:
#                 prev=curr
#                 curr=curr.next
#         return dummy.next

        