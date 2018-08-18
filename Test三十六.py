"""
题目:
输入两个链表，找出它们的第一个公共节点
"""

class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None

class Solution:
	"""
	思路一:
	两条相交的链表呈Y型，可以从两条链表尾部同时出发，最后一个相同的节点
	就是链表的第一个相同的节点，可以利用栈来实现
	"""
	def FindFirstCommonNode(self,pHead1,pHead2):
		if not pHead1 or not pHead2:
			return None
		stack1=[]
		stack2=[]
		while pHead1:
			stack1.append(pHead1.val)
			pHead1=pHead1.next
		while pHead2:
			stack2.append(pHead2.val)
			pHead2=pHead2.next
		first=None
		while stack1 and stack2:
			top1=stack1.pop()
			top2=stack2.pop()
			if top1 == top2:
				first=top1
			else:
				break
		return first

	"""
	思路二:
	可以让其中长的链表先走几步，剩余的长度到短链表的长度相同
	"""
	def FindFirstCommonNodeTwo(self,pHead1,pHead2):
		if not pHead1 or not pHead2:
			return None
		p1,p2=pHead1,pHead2
		length1=length2=0
		while p1:
			length1+=1
			p1=p1.next
		while p2:
			length2+=1
			p2=p2.next
		if length1>length2:
			while length1 - length2:
				pHead1=pHead1.next
				length1-=1
		else:
			while length2 - length1:
				pHead2=pHead2.next
				length2-=1

		while pHead1 and pHead2:
			if pHead1.val == pHead2.val:
				return pHead1
			pHead1=pHead1.next
			pHead2=pHead2.next
		return None

if __name__=='__main__':
	L1=ListNode(1)
	L1.next=ListNode(2)
	L1.next.next=ListNode(3)
	L1.next.next.next=ListNode(4)
	L2=ListNode(3)
	L2.next=ListNode(6)
	L2.next.next=ListNode(3)
	L2.next.next.next=ListNode(4)
	S=Solution()
	first1=S.FindFirstCommonNode(L1, L2)
	print(first1)
	first2=S.FindFirstCommonNodeTwo(L1, L2)
	print(first2.val)

