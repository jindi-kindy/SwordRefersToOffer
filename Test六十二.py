"""
题目:
给定一颗二叉搜索树，找出其中的第k大的结点
"""
class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None

class Solution:
    def KthNode(self,pRoot,k):
        self.res=[]
        self.dfs(pRoot)
        return self.res[k-1] if 0<k<=len(self.res) else None

    def dfs(self,pRoot):
        if not pRoot:
            return None
        self.dfs(pRoot.left)
        self.res.append(pRoot)
        self.dfs(pRoot.right)



root=TreeNode(10)
root.left=TreeNode(6)
root.right=TreeNode(14)
root.left.left=TreeNode(4)
root.left.right=TreeNode(8)
root.right.left=TreeNode(12)
root.right.right=TreeNode(16)

S=Solution()
res=S.KthNode(root,2)
print(res.val)