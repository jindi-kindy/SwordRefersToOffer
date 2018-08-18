"""
题目:
在一个长度为n的数组里的所有数字都在0到n-1的范围内，数组中某些数字是重复的，但不知道有几个数字是重复的
也不知道数字重复几次，请找出数组中任意一个重复的数字
"""
def duplicate(numbers,duplication):
	for i in range(len(numbers)):
		if numbers[i] in numbers[i+1:]:
			duplication[0]=numbers[i]
			return True
	return False

array={}
re=duplicate('1224568',array)
print(re,array[0])