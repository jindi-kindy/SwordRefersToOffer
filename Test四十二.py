"""
题目:
输入一个递增排序的数组和一个数字S，在数组中查找两个数，他们的和正好是S
如果有多对数字的和等于S，输出两个数的乘积最小的
"""
class Solution:
	def FindNumberWithSum(self,array,tsum):
		for i in array:
			if tsum-i in array:
				if tsum-i==i:
					if array.count(i)>1:
						return [i,i]
				else:
					return [i,tsum-i]
		return []

S=Solution()
res=S.FindNumberWithSum([1,2,4,7,11,15],15)
print(res)					
						
