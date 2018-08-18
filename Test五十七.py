"""
题目:
给定一个二叉树和其中一个节点，请找出中序遍历顺序的下一个结点并且返回，树中的结点不仅包含左右子结点，同时包含指向父节点的指针
思路:
如果一个结点有右子树，那么它的下一个结点就是它的右子树的最左子结点，也就是说从右子结点出发一直沿着指向左子树结点的指针，就能找到
它的下一个结点
结点没有右子树的情形，如果结点是它父节点的左子结点，那么它的下一个结点就是它的父节点
如果一个结点既没有右子树，并且它还是父节点的右子节点，可以沿着指向父节点的指针一直向上遍历，知道找到一个是它父节点的左子结点的节点，如果这样
的节点存在，那么这个节点的父节点就是要找的下一个结点
"""
class TreeLinkNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None
		self.next=None


class Solution:
    def GetNext(self, pNode):
        #如果当前节点为空
        if pNode==None:
            return None
        #如果当前节点是根节点，而且没有孩子节点
        if pNode.next==None and pNode.left==None and pNode.right==None:
            return None
        #有右子树
        if pNode.right!=None:
            return self.GetFirst(pNode.right)
        #没有右子树
        else:
            #当前节点不是根节点，而且没有右子树
            if pNode.next!=None :
                father=pNode.next
                #如果当前节点是它父亲节点的左子树，就返回父节点
                if father.left==pNode:
                    return father
                #如果当前节点是它父亲节点的右子树，就一直往上找，找到祖父节点，直到找到根节点或者找到了当前所在子树是左子树为止
                else:
                    if father.next!=None:
                        f_father=father.next
                        while f_father.next!=None and f_father.right==father:
                            f_father=f_father.next
                            father=f_father
                        #如果所在子树还是右子树，则已经找到了根节点部分，返回空
                        if  f_father.right==father:
                            return None
                        else:
                            return f_father
                    return None
            else:
                return None

    def GetFirst(self,pNode):
        if pNode.left==None:
            return pNode
        else:
            return self.GetFirst(pNode.left)
T=TreeLinkNode('a')
T.left=TreeLinkNode('b')
T.right=TreeLinkNode('c')
T.left.left=TreeLinkNode('d')
T.left.right=TreeLinkNode('e')
T.left.right.left=TreeLinkNode('h')
T.left.right.right=TreeLinkNode('i')
T.right.left=TreeLinkNode('f')
T.right.right=TreeLinkNode('g')
T.left.next=T
T.right.next=T
T.left.left.next=T.left
T.left.right.next=T.left
T.left.right.left.next=T.left.right
T.left.right.right.next=T.left.right
T.right.next=T
T.right.left.next=T.right
T.right.right.next=T.right
S=Solution()
R=S.GetNext(T.right.right)
print(R)
		