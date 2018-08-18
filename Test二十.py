"""
题目:
定义栈的数据结构，在类型中实现一个能够得到栈最小元素的min函数

思路:
每入栈一次，就与辅助栈顶比较大小，如果小就入栈，如果大就入栈顶当前的辅助栈顶
出栈时 ，辅助栈也要出栈
这样就可以保证辅助栈顶一定都是当前栈的最小值
"""
class Solution:
	def __init__(self):
		self.stack=[]
		self.assist=[]
	def push(self,node):
		min=self.min()
		if not min or node < min:
			self.assist.append(node)
		else:
			self.assist.append(min)

		self.stack.append(node)
	def pop(self):
		if slef.stack:
			self.assist.pop()
			return self.stack.pop()
	def top(self):
		if self.stack:
			return self.stack[-1]
	def min (self):
		if self.assist:
			return self.assist[-1]
	def minx(self):
		if self.assist:
			return self.assist[-1]


S=Solution()
S.push(6)
S.push(2)
S.push(3)
S.push(2)
S.push(5)
print(S.stack)
print(S.assist)
print(S.minx())