# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class queue:
    def __init__(self):
        self.q=[]
        self.front=-1
    def push(self,x):
        if(self.front==-1):
            self.front=0
            self.q.append(x)
        else:
            self.q.append(x)
    def pop(self):
        if(self.front==-1):
            return 
        else:
            x=self.q[self.front]
            self.front+=1
            if(len(self.q)==self.front):
                self.q=[]
                self.front=-1
            return x
    def size(self):
        if self.front==-1:
            return 0
        else:
            return len(self.q)-self.front

            
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=queue()
        ans=[]
        q.push(root)
        while(q.size()>0):
            l=q.size()
            level=[]
            for i in range(l):
                node=q.pop()
                level.append(node.val)
                if(node.left!=None):
                    q.push(node.left)
                if(node.right!=None):
                    q.push(node.right)
            ans.append(level)
        return ans