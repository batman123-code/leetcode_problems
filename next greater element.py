# class Solution:
#     def nextGreaterElement(self, nums1: List[int], arr: List[int]) -> List[int]:
#         n=len(arr)
#         ans={}
#         stack=[]
#         for i in range(n-1,-1,-1):
#             while(len(stack)>0 and stack[-1]<=arr[i]):
#                 stack.pop()
#             if(len(stack)==0):
#                 ans[arr[i]]=-1
#             else:
#                 ans[arr[i]]=stack[-1]
#             stack.append(arr[i])
#         return list(map(lambda x:ans[x],nums1))
