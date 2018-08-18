"""
题目:
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如
输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
则重建二叉树并返回。


思路:
前序遍历:先访问根结点，再访问左子结点，最后访问右子结点
中序遍历:先访问左子结点，再访问根结点，最后访问右子结点
后序遍历:先访问左子结点，再访问右子结点，最后访问根结点
"""
class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None

def reConstructBinaryTree(pre,tin):
    if len(pre) == 0:
        return None
    elif len(pre) == 1:
        return TreeNode(pre[0])
    else:
        root = TreeNode(pre[0])
        pos = tin.index(pre[0])
        root.left = reConstructBinaryTree(pre[1:pos + 1], tin[:pos])
        root.right = reConstructBinaryTree(pre[pos + 1:], tin[pos + 1:])
    return root

root=reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
print(root.val)
print(root.left.val)
print(root.left.left.val)
print(root.left.left.right.val)