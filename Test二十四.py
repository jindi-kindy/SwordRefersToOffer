"""
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径
路径定义为从树的根节点开始往下一直到叶洁点所经过的结点形成一条路径
"""
class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None

def reConstructBinaryTree(pre,tin):
	if len(pre)==0:
		return None
	elif len(pre)==1:
		return TreeNode(pre[0])
		
	else:
		root=TreeNode(pre[0])
		pos=tin.index(pre[0])
		root.left=reConstructBinaryTree(pre[1:pos+1], tin[:pos])
		root.right=reConstructBinaryTree(pre[pos+1:], tin[pos+1:])
	return root





class Solution:
    def FindPath(self,root,expectNumber):
        if root==None:
        	return []
        if root.left==None and root.right==None and expectNumber==root.val:
        	return [[root.val]]
        if root.left==None and root.right==None and expectNumber!=root.val:
        	return []

        res=[]
        res_left=self.FindPath(root.left, expectNumber-root.val)
        res_right=self.FindPath(root.right, expectNumber-root.val)
        for i in res_left+res_right:
        	res.append([root.val]+i)
        return res 


if __name__=='__main__':
	root1=reConstructBinaryTree([1,2,3,5], [3,2,1,5])
	root=TreeNode(1)
	root.left=TreeNode(2)
	root.right=TreeNode(3)
	root.left.left=TreeNode(1)
	root.left.right=TreeNode(3)
	root.right.left=TreeNode(1)
	root.right.right=TreeNode(2)

	S=Solution()
	res=S.FindPath(root,6)
	print(res)