"""
题目:
操作给定的二叉树，将其变换为源二叉树的镜像

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
	def Mirror(self,root):
		if (root==None or (root.left==None and root.right==None)):
			return None
		tmp=root.left
		root.left=root.right
		root.right=tmp
		if root.left:
			self.Mirror(root.left)
		if root.right:
			self.Mirror(root.right)
			
if __name__=='__main__':
	root1=reConstructBinaryTree([1,2,4,5,3,6,7], [4,2,5,1,6,3,7])
	print(root1.val)
	print(root1.left.val)
	print(root1.right.val)
	S=Solution()
	S.Mirror(root1)
	print(root1.left.val)

