"""
题目:
在一个排序的链表中，存在重复的节点，删除该链表中重复的节点，重复的结点不保留，返回链表头指针
"""
class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None


class Solution:
	#把所有节点的值放到一个列表中，筛选出户值数量为1的值，再新建一个链表返回即可
	def deleteDupication(self,pHead):
		res=[]
		while pHead:
			res.append(pHead.val)
			pHead=pHead.next
		res=list(filter(lambda c:res.count(c)==1, res))
		dummy=ListNode(0)
		pre=dummy
		for i in res:
			node=ListNode(i)
			pre.next=node
			pre=pre.next
		return dummy.next
	def deleteDupication2(self,pHead):
		if pHead==None or pHead.next==None:
			return pHead
		new_head=ListNode(-1)
		new_head.next=pHead
		pre=new_head
		p=pHead
		nex=None
		while p!=None and p.next!=None:
			nex=p.next
			if p.val==nex.val:
				while nex!=None and nex.val ==p.val:
					nex=nex.next
				pre.next=nex
				p=nex
			else:
				pre=p
				p=p.next
		return new_head.next




L=ListNode(1)
L.next=ListNode(3)
L.next.next=ListNode(3)
L.next.next.next=ListNode(4)
L.next.next.next.next=ListNode(4)
L.next.next.next.next.next=ListNode(6)
L1=ListNode(None)
S=Solution()
dummy=S.deleteDupication(L)
print(dummy.next.val)
new_head=S.deleteDupication2(L1)
print(new_head.val)