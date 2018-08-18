"""
题目:
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是
"""
class Solution:
	def isNumeric(self,s):
		if len(s)<0:
			return False
		has_sign=False
		has_point=False
		has_e=False
		for i in range(len(s)):
			#对于e的情况
			if s[i]=='E' or s[i]=='e':
				#不能同时出现两个e
				if has_e:
					return False
				#e不能出现在最后面，因为e后面要接数字
				else:
					has_e=True
					if i==len(s)-1:
						return False
			#如果前面已经出现过了符号位，那么这个符号位，必须跟在e后面
			elif s[i]=='+' or s[i]=='-':
				if has_sign:
					if s[i-1]!='e' and s[i-1]!='E':
						return False
				else:
					has_sign=True
					if i>0 and s[i-1]!='e' and s[i-1]!='E':
						return False
			#对于小数点的情况
			elif s[i]=='.':
				#小数点不能出现两次，而且如果已经出现过e了，那么就不能再出现小数点
				if has_point or has_e:
					return False
				else:
					has_point=True
					if has_e:
						return False
			else:
				if s[i]<'0' or s[i]>'9':
					return False
		return True

S=Solution()
flag=S.isNumeric('-.123')
print(flag)