"""
题目:
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹
出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列
4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的
弹出序列。（注意：这两个序列的长度是相等的）

"""
class Solution:
	def IsPopOrder(self,pushV,popV):
		if len(popV)==0 or len(pushV)!=len(popV):
			return False
		stackData=[]
		for i in pushV:
			stackData.append(i)
			while len(stackData) and stackData[-1]==popV[0]:
				stackData.pop()
				popV.pop(0)
		if len(stackData):
			return False
		return True

S=Solution()
print(S.IsPopOrder([1,2,3,4,5], [4,5,1,2,3]))