"""
输入两个单调递增的链表，输出两个链表合成后的链表

"""
class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None

	

#生成链表
def List(array):
	if len(array)==0:
		return None
	elif len(array)==1:
		return ListNode(array[0])
	else:
		rList=ListNode(array[0])
		rList.next=List(array[1:])
	return rList

class Solution:
	def Merge(self,pHead1,pHead2):
		if not pHead1:
			return pHead2
		if not pHead2:
			return pHead1
		pMergeHead=None
		p_merge=[]
		if pHead1.val<pHead2.val:
			pMergeHead=pHead1
			pMergeHead.next=self.Merge(pHead1.next, pHead2)
		else:
			pMergeHead=pHead2
			pMergeHead.next=self.Merge(pHead1, pHead2.next)
		return pMergeHead



if __name__=='__main__':
	L=ListNode
	pHead1=List([1,3,6,8,9])
	pHead2=List([2,4,5,7,10])
	S=Solution()
	p_merge=[]
	pMergeHead=S.Merge(pHead1, pHead2)	
	while  pMergeHead:
		p_merge.append(pMergeHead.val)
		pMergeHead=pMergeHead.next
	print(p_merge)