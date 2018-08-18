"""
题目:
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
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

def PrintFromTopToBottom(root):
	if not root:
		return []
	result=[]
	tmp=[root]
	while len(tmp):
		cur=tmp.pop(0)
		result.append(cur.val)
		if cur.left:
			tmp.append(cur.left)
		if cur.right:
			tmp.append(cur.right)
	return result

if __name__=='__main__':
	root1=reConstructBinaryTree([1,2,4,5,3,6,7], [4,2,5,1,6,3,7])
	result=PrintFromTopToBottom(root1)
	print(result)