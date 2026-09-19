# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        target=TreeNode(val)
        if root is None:
            return target
        curr=root
        while(curr!=None):
            if(target.val<curr.val):
                if(curr.left!=None):
                    curr=curr.left
                else:
                    curr.left=target
                    break
            if(target.val>curr.val):
                if(curr.right!=None):
                    curr=curr.right
                else:
                    curr.right=target
                    break
        return root