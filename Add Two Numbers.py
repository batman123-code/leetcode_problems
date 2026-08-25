# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         curr1=l1
#         c=0
#         curr2=l2
#         ans=ListNode(-1)
#         curr3=ans
#         while(curr1!=None or curr2!=None ):
            
#             total=c
#             c=0
#             if(curr1!=None):
#                 total+=curr1.val
#                 curr1=curr1.next
#             if(curr2!=None):
#                 total+=curr2.val
#                 curr2=curr2.next
#             if(total>=10):
#                 c=1
#                 total-=10
#             new_node=ListNode(total)
#             curr3.next=new_node
#             curr3=new_node
#             if(c>0):
#                 new_node=ListNode(c)
#                 curr3.next=new_node
#         return ans.next
        