"""
题目:
将一个字符转换成一个整数，要求不能使用字符串转换整数的库函数，数值为0或者字符换不是一个合法的数值则返回0
"""
class Solution:
	def StrToInt(self,s):
		numlist=['0','1','2','3','4','5','6','7','8','9','+','-']
		label=1
		sum=0
		if s=="":
			return 0
		for string in s:
			if string in numlist:
				if string=='+':
					label=1
					continue
				elif string=='-':
					label=-1
					continue
				else:
					sum=sum*10+numlist.index(string)
			else:
				sum=0
				break
		return sum*label

S=Solution()
str=S.StrToInt('+12448f9404')
print(str)