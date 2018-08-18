"""
题目:
输入一个整数，输出该数二进制表示中1的个数，其中负数用补码表示
思路:
把一个整数减去1，再和原整数做与运算，会把改整数最右边一个1变成0。
那么一个整数的二进制表示中有多少个1，就可以进行多次这样的操作。
"""



def Sort(number):
	count=0
	if number<0:
		number=number&0x7FFFFFFF
		count+=1
	while number:
		count+=1
		number=(number-1)&number
	return count

print(Sort(-3))

