# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         length=0
#         last=head
#         if(head==None or head.next==None):
#             return head
#         else:
#             while(last.next!=None):
#                 last=last.next
#                 length+=1
#             length+=1
#             k=k%length
#             if(k==0):
#                 return head
#             else:
#                 curr=head
#                 for i in range(length-k-1):
#                     curr=curr.next
#                 last.next=head
#                 head=curr.next
#                 curr.next=None
#         return head
