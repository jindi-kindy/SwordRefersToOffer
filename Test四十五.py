"""
题目:
给5张牌，根据规则判断这副牌是否是顺子
"""
class Solution:
	def IsContinuous(self,numbers):
		if not numbers:
			return False
		numbers.sort()

		zeronum=numbers.count(0)
		for i,v in enumerate(numbers[:-1]):
			if v!=0:
				if numbers[i+1]==v:
					return False
				zeronum=zeronum - (numbers[i+1] - v)+1
				if zeronum<0:
					return False
		return True

S=Solution()
flag=S.IsContinuous([4,5,1,0,0])
print(flag)