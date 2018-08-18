"""
题目:
输入一颗二叉树，判断该二叉树是否是平衡二叉树
思路:
平衡二叉树的定义是:所谓的平衡之意，就是树中任意一个节点下左右两个子树的高度
差不超过1
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
	"""
	使用后序遍历，每次遍历统计当前节点的左子树和右子树的高度，并比较左右子树
	的高度差，当高度差超过1，该二叉树不属于平衡二叉
	"""
	def IsBalanced_Solution(self,root):
		if not root:
			return True
		if abs(self.maxDepth(root.left)-self.maxDepth(root.right))>1:
			return False
		return self.IsBalanced_Solution(root.left) and self.IsBalanced_Solution(root.right)
	def maxDepth(self,root):
		if not root:
			return 0
		return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

if __name__=='__main__':
	root=TreeNode(10)
	root.left=TreeNode(6)
	root.right=TreeNode(14)
	root.left.left=TreeNode(4)
	root.left.right=TreeNode(8)
	root.right.left=TreeNode(12)
	root.right.right=TreeNode(16)
	root.left.left.left=TreeNode(9)
	#root.left.left.left.left=TreeNode(9)
	S=Solution()
	flag=S.IsBalanced_Solution(root)
	print(flag)