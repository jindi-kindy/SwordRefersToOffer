"""
题目:
输入一颗二叉搜索树，将该二叉搜索树转换成一个排序的双向链表，不能创建任何新的节点，
只能调整树中结点指针的指向
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
	def Convert(self,pRootOfTree):
		root=pRootOfTree
		if not root:
			return None
		pHead=root
		while pHead.left:
			pHead=pHead.left
		self.helpConvert(root)
		return pHead

	def helpConvert(self,root):
		#节点为叶子节点
		if not root.left and not root.right:
			return 
		#对左子树进行递归，找到左子树的最右一个节点，并和root节点连起来
		if root.left:
			preRoot=root.left
			self.helpConvert(root.left)
			#找到左子树的最右边节点，和root节点连起来
			while preRoot.right:
				preRoot=preRoot.right
			root.left=preRoot
			preRoot.right=root
		#右子树
		if root.right:
			nextRoot=root.right
			self.helpConvert(root.right)
			while nextRoot.left:
				nextRoot=nextRoot.left
			root.right=nextRoot
			nextRoot.left=root
if __name__=='__main__':
	root=TreeNode(10)
	root.left=TreeNode(6)
	root.right=TreeNode(14)
	root.left.left=TreeNode(4)
	root.left.right=TreeNode(8)
	root.right.left=TreeNode(12)
	root.right.right=TreeNode(16)
	S=Solution()
	S.Convert(root)