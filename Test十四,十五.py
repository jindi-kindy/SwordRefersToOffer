"""
题目:
输入一个链表，输出该链表中倒数第k个结点
"""
class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None

#生成一个链表
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
	#找到链表倒数第k个元素
    def FindKthToTail(self, head, k):
        front=head
        later=head

        for i in range(k):
        	if front==None:
        		return
        	if front.next==None and i==k-1:
        		return head
        	front=front.next
        while front.next!=None:
        	front=front.next
        	later=later.next
        return later.next

    #输入一个链表，反转链表后，输出链表的所有元素
    def ReverseList(self,pHead):
    	if not pHead or not pHead.next:
    		return pHead
    	last=None
    	while pHead:
    		tmp=pHead.next
    		pHead.next=last
    		last=pHead
    		pHead=tmp
    	return last

if __name__=='__main__':
	array=[4,5,6,3,4,1,7,8,0,9,8]
	rList=List(array)

	S=Solution()
	#找到链表倒数第k个元素
	Find=S.FindKthToTail(rList,3)
	print(Find.val)
	Reverse=S.ReverseList(rList)
	print(Reverse.next.val)