"""
题目:
输入一个字符串，按照字典打印出该字符串中字符的所有排列，例如输入字符串abc,
则打印出有字符串a,b,c所能排列出来的所有字符串
"""
class Solution:
	def Permutation(self,ss):
		res=[]
		def Traversal(ss,join_ss=''):
			if ss:
				for i,s in enumerate(ss):
					sub_ss=ss[:i]+ss[i+1:]
					Traversal(sub_ss,join_ss+s)
			elif join_ss and join_ss not in res:
				res.append(join_ss)
		if ss:
			Traversal(ss)
		return res
S=Solution()
res=S.Permutation('eea')
print(res)