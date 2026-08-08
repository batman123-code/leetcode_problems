# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.


# two iteration

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         curr=head
#         length=0
#         while(curr!=None):
           
#             curr=curr.next
#             length+=1
#         mid=length//2
#         curr=head
#         for i in range(mid):
#             curr=curr.next
#         return curr



# using fast and slow pointer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         fast=head
#         slow=head
#         while(fast!=None and fast.next!=None):
#             slow=slow.next
#             fast=fast.next.next
#         return slow
            


 