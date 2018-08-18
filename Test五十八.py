"""
题目:
实现一个函数，用来判断一颗二叉树是不是对称的
"""
class TreeLinkNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None
		self.next=None

class Solution():
    #如果二叉树同此二叉树的镜像是同样的，定义其为对称的
    #构造镜像树
    def isSymmetrical(self,pRoot):
        tree1=self.copy(pRoot)
        tree2=self.Mirror(pRoot)
        return self.compare(tree1,tree2)
    def Mirror(self, pRoot):
        if (pRoot == None or (pRoot.left == None and pRoot.right == None)):
            return None
        tmp = pRoot.left
        pRoot.left = pRoot.right
        pRoot.right = tmp
        if pRoot.left:
            self.Mirror(pRoot.left)
        if pRoot.right:
            self.Mirror(pRoot.right)
        return pRoot

    #复制二叉树
    def copy(self,pRoot):
        if pRoot==None:
            return None
        node=TreeLinkNode(pRoot.val)
        node.left=self.copy(pRoot.left)
        node.right=self.copy(pRoot.right)
        return node
    #比较二叉树和二叉镜像树
    def compare(self,tree1,tree2):
        if not tree1 and not tree2:
            return True
        if tree1 and tree2 and tree1.val==tree2.val:
            return self.compare(tree1.left,tree2.left) and self.compare(tree1.right,tree2.right)
        else:
            return False
    #直接遍历比较
    def isSymmetrical2(self,pRoot):
        if not pRoot:
            return True
        return self.compareNodeVal(pRoot,pRoot)
    def compareNodeVal(self,pRoot1,pRoot2):
        if pRoot1 is None and pRoot2 is None:
            return True
        if pRoot1 is None or pRoot2 is None:
            return False
        if pRoot1.val!=pRoot2.val:
            return False
        return self.compareNodeVal(pRoot1.left,pRoot2.right) and self.compareNodeVal(pRoot1.right,pRoot2.left)



T=TreeLinkNode(8)
T.left=TreeLinkNode(6)
T.right=TreeLinkNode(6)
T.left.left=TreeLinkNode(5)
T.left.right=TreeLinkNode(7)
T.right.left=TreeLinkNode(7)
#T.right.right=TreeLinkNode(5)
S=Solution()
flag=S.isSymmetrical(T)
flag1=S.isSymmetrical2(T)
print(flag1)
