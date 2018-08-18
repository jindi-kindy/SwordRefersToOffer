"""
题目:
一个链表中包含环，请找出该链表的环的入口结点
"""
class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None
class Solution:
	def EntryNodeOfLoop(self,pHead):
		slow,fast=pHead,pHead
		while fast and fast.next:
			slow=slow.next
			fast=fast.next.next
			if slow==fast:
				slow2=pHead
				while slow != slow2:
					slow=slow.next
					slow2=slow2.next
				return slow
		return False

L=ListNode(1)
L.next=ListNode(2)
L.next.next=ListNode(3)
L.next.next.next=ListNode(4)
L.next.next.next.next=ListNode(5)
L.next.next.next.next.next=L.next.next


S=Solution()
J=S.EntryNodeOfLoop(L)
print(J.val)
