"""
题目:
实现一个函数按照之字行打印二叉树，第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，
其他行以此类推
"""
class TreeLinkNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None

class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        nodestack=[pRoot]
        result=[]
        while nodestack:
            res=[]
            nextstack=[]
            for i in nodestack:
                res.append(i.val)
                if i.left:
                    nextstack.append(i.left)
                if i.right:
                    nextstack.append(i.right)
            nodestack=nextstack
            result.append(res)
        returnResult=[]
        for i,v in enumerate(result):
            if i%2==0:
                returnResult.append(v)
            else:
                returnResult.append(v[::-1])
        return returnResult





T=TreeLinkNode(1)
T.left=TreeLinkNode(2)
T.right=TreeLinkNode(3)
T.left.left=TreeLinkNode(4)
T.left.right=TreeLinkNode(5)
T.right.left=TreeLinkNode(6)
T.right.right=TreeLinkNode(7)
S=Solution()
result=S.Print(T)
print(result)