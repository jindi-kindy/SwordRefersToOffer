"""
题目:
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的
前半部分，偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变
思路:
创建双向队列，遍历数组，奇数前插入，偶数后插入
"""
from collections import deque
class Solution:
	def reOrderArray(self,array):
		odd=deque()
		l=len(array)
		for i in range(l):
			if array[l-i-1]%2 !=0:
				odd.appendleft(array[-i-1])
			if array[i] % 2==0:
				odd.append(array[i])
		return odd

if __name__=='__main__':
	S=Solution()
	order=S.reOrderArray([2,3,4,7,1,3,8])
	print(order)
