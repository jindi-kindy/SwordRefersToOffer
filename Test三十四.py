"""
在一个字符串中找到第一个只出现一次的字符，并返回它的位置
"""
class Solution:
	def FirstNotRepeatingChar(self,s):
		length=len(s)
		if length==0:
			return -1
		item={}
		for i in range(length):
			if s[i] in item:
				item[s[i]]+=1
			else:
				item[s[i]]=1
		for i in range(length):
			if item[s[i]]==1:
				return i 

		return -1

S=Solution()
print(S.FirstNotRepeatingChar('aaaaabbbbvvv'))