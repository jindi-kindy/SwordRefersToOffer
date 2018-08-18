"""
输入一个复杂链表(每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点)
返回结果为复制后复杂链表的head


"""
class RandomListNode:
	def __init__(self,x):
		self.label=x
		self.next=None
		self.random=None




class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
         
        dummy = pHead
         
        # first step, N' to N next
        while dummy:
            dummynext = dummy.next
            copynode = RandomListNode(dummy.label)
            copynode.next = dummynext
            dummy.next = copynode
            dummy = dummynext
         
        dummy = pHead
         
        # second step, random' to random'
        while dummy:
            dummyrandom = dummy.random
            copynode = dummy.next
            if dummyrandom:
                copynode.random = dummyrandom.next
            dummy = copynode.next
         
        # third step, split linked list
        dummy = pHead
        copyHead = pHead.next
        while dummy:
            copyNode = dummy.next
            dummynext = copyNode.next
            dummy.next = dummynext
            if dummynext:
                copyNode.next = dummynext.next
            else:
                copyNode.next = None
            dummy = dummynext
 
        return copyHead


if __name__=='__main__':
	Label=RandomListNode('A')
	Label.next=RandomListNode('B')
	Label.random=RandomListNode('C')
	Label.next.next=RandomListNode('C')
	Label.next.next.next=RandomListNode('D')
	Label.next.next.next.random=RandomListNode('B')
	Label.next.next.next.next=RandomListNode('E')
	S=Solution()
	newNode=S.Clone(Label)
	print(newNode)