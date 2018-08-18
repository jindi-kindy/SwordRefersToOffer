"""
输入一颗二叉树，求该树的深度
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
	#使用递归方法
	def TreeDepth(self,pRoot):
		if pRoot is None:
			return 0
		"""
		如果该树只有一个节点，它的深度为1，如果根节点只有左子树没有右子树，
		如果树的深度为左子树的深度加1，同样，如果只有右子树没有左子树，那么
		树的深度为右子树的深度加1，如果既有左子树也有y右子树，那么该树的深度
		就是左子树和右子树的最大值加1
		"""
		count=max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))+1
		return count

class Solution1:
	#方法二,使用队列
	def levelOrder(self,root):
		#存储最后层次遍历的结果
		res=[]
		#层数
		count=0
		#如果根节点为空，则返回空列表
		if root is None:
			return count
		q=[]
		#首先将根节点入队
		q.append(root)
		#列表为空时，循环终止
		while len(q)!=0:
			#使用列表存储同层节点
			tmp=[]
			#记录同层节点的个数
			length=len(q)
			for i in range(length):
				#将同层节点依次出队
				r=q.pop(0)
				if r.left is not None:
					#非空左孩子入队
					q.append(r.left)
				if r.right is not None:
					q.append(r.right)
				tmp.append(r.val)
			if tmp:
				count+=1
			res.append(tmp)
		return count
	def TreeDepth(self,pRoot):
		if pRoot is None:
			return 0
		count=self.levelOrder(pRoot)
		return count



if __name__=='__main__':
	root=TreeNode(10)
	root.left=TreeNode(6)
	root.right=TreeNode(14)
	root.left.left=TreeNode(4)
	root.left.right=TreeNode(8)
	root.right.left=TreeNode(12)
	root.right.right=TreeNode(16)
	root.left.left.left=TreeNode(9)
	S=Solution()
	count=S.TreeDepth(root)
	print(count )
	S1=Solution1()
	count1=S1.TreeDepth(root)
	print(count1)