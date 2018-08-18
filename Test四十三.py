"""
题目:
对于一个给定的字符序列S，把其循环左移K位后的序列输出
"""
class Solution:
	def LeftRotateString(self,s,n):
		if not s:
			return ""
		l=list(s)
		m=len(l)
		a=[]
		for i in range(m):
			if i+n<m:
				a.append(l[i+n])
		for i in range(n):
			a.append(l[i])
		return ''.join(a)

	def LeftRotateString2(self,s,n):
		return s[n:]+s[:n]

S=Solution()
s=S.LeftRotateString('abcXYZdef', 3)
print(s)
s1=S.LeftRotateString2('abcXYZdef', 3)
print(s1)