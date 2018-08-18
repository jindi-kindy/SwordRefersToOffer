"""
题目：
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字，例如输入一个
长度为9的数组[1,2,3,2,2,2,5,4,2],由于数字2在数组中出现了5次，超过了数组长度的一半，因此输出
2，如果不存在则输出0
"""
class Solution:
	def MoreThanHalfNum_Solution(self,numbers):
		dict={}
		for i in numbers:
			if i in dict:
				dict[i]+=1
			else:
				dict[i]=1
			if dict[i] > len(numbers)/2:
				return i
		return 0


S=Solution()
e=S.MoreThanHalfNum_Solution([1,2,2,7,2,2,5,4,2])
print(e)