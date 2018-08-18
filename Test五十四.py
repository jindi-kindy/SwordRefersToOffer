"""
题目:
请实现一个函数用来找出字符流中第一个只出现一次的字符
"""
class Solution:
	def __init__(self):
		self.s=""
	def FirstAppearingOnce(self):
		for a in self.s:
			if self.s.count(a)==1:
				return a
		return '#'
	def Insert(self,char):
		self.s+=char


S=Solution()
S.Insert('aabbcc')
first=S.FirstAppearingOnce()
print(first)