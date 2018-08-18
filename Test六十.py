"""
题目:
从上到下按层打印二叉树，同一层结点从左至右输出，每一层输出一行
"""
class TreeLinkNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None

class Solution:
    def Print(self,pRoot):
        if not pRoot:
            print('None')
        nodestack=[pRoot]
        result=[]
        while nodestack:
            nextstack=[]
            res=[]
            for i in nodestack:
                res.append(i.val)
                if i.left:
                    nextstack.append(i.left)
                if i.right:
                    nextstack.append(i.right)
            nodestack=nextstack
            result.append(res)
        for i,v in enumerate(result):
            for i in range(0,len(v)):
                print(v[i],end="")
            print('\n')



T=TreeLinkNode(1)
T.left=TreeLinkNode(2)
T.right=TreeLinkNode(3)
T.left.left=TreeLinkNode(4)
T.left.right=TreeLinkNode(5)
T.right.left=TreeLinkNode(6)
T.right.right=TreeLinkNode(7)
S=Solution()
S.Print(T)
