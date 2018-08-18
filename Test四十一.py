"""
题目:
输出所有和为S的连续整数序列。序列内按照从小到大的顺序，
序列间按照开始数字从小到大的顺序
"""
class Solution:
	def FindContinuousSequence(self,tsum):
		res=[]
		for i in range(1,tsum//2+1):
			sumRes=i
			for j in range(i+1,tsum//2+2):
				sumRes+=j
				if sumRes==tsum:
					res.append(list(range(i,j+1)))
					break
				elif sumRes>tsum:
					break
		return res

S=Solution()
res=S.FindContinuousSequence(3)
print(res)