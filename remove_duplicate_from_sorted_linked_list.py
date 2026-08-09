# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         curr = head
#         if (head == None):
#             return head
#         elif (head.next == None):
#             return head
        
#         while (curr != None and curr.next != None):
#             if (curr.val == curr.next.val):
#                 curr.next = curr.next.next
#             else:
#                 curr = curr.next
                
#         return head