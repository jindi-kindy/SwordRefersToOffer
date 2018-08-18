"""
题目:
单词翻转
"""
class Solution:
	def ReverseSentence(self,s):
		return ' '.join(s.split(' ')[::-1])

S=Solution()
s=S.ReverseSentence('student a am I')
print(s)