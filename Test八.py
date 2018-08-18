"""
一直青蛙一次可以跳上一级台阶，也可以跳上2级，
求该青蛙跳上一个n级的台阶总共有多少种跳法

首先我们考虑最简单的情况。如果只有1级台阶，那么显然只一种跳法。
如果有2级台阶，那就有两种跳法：一种是分两次跳，每次跳1级；另一种是一次跳2级。
接着，我们来讨论一般情况。我们把n级台阶时的跳法看成是n的函数，记为f(n)。当n>2时，
第一次跳的时候就有两种不同的选择：一是第一次只跳1级，此时跳法数目等于后面剩下的
n-1级台阶的跳法数目，即为f(n-1)；另外一种选择是跳一次跳2级，此时跳法数目等于后
面剩下的n-2级台阶的跳法数目，即为f(n-2)。因此n级台阶的不同跳法的总数f(n)=f(n-1)+f(n-2)。
分析到这里，我们不难看出这实际上就是斐波那契数列了。
"""
class Solution:
	def jumpFloor(self,number):
		if number<3:
			return number
		first,second,third=1,2,0
		for i in range(3,number+1):
			third=first+second
			first=second
			second=third
		return third

	#青蛙一次可以跳1级，2级....n级
	#跳法f(n)=2^(n-1)。
	def BjumpFloor(self,number):
		if number<=2:
			return number
		total=1
		for _ in range(1,number):
			total*=2
		return total

if __name__=='__main__':
	S=Solution()
	Fn=S.jumpFloor(10)
	print(Fn)