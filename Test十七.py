"""
题目:
输入两颗二叉树A,B,判断B是不是A的子结构
思路:
要查找树A中是否存在和树B结构一样的子树，可以分为两步:第一步在树A中
找到和B的根结点的值一样的结点R，第二步在判断树A中以R为根节点的子树是不是包含和
树B一样的结构
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
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2) or self.is_subtree(pRoot1, pRoot2)
    def is_subtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)	
root1=reConstructBinaryTree([1,2,4,5,3,6,7], [4,2,5,1,6,3,7])
root2=reConstructBinaryTree([2,4,5], [4,2,5])

S=Solution()
flag=S.HasSubtree(root1, root2)
print(flag)
