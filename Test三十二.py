"""
题目:
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所
有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""
from itertools import permutations
class Solution:
	def PrintMinNumber(self,numbers):
		x=list(permutations(sorted(list(numbers))))
		new_data=set()
		for i in x:
			n_str="".join([str(n) for n in i])
			new_data.add(n_str)
		min_n=sorted(list(new_data))[0]
		print(min_n)

S=Solution()
S.PrintMinNumber({3,32,321})