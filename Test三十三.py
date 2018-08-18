"""
题目:
把只包含因子2，3和5的数称作丑数习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

思路:
所谓的一个数m是另一个数n的因子，是指n能被m整除，也就是n%m==0。根据丑数的定义，
丑数只能被2、3和5整除。根据丑数的定义，丑数应该是另一个丑数乘以2、3或者5的结果
（1除外）。因此我们可以创建一个数组，里面的数字是排好序的丑数，每一个丑数都是
前面的丑数乘以2、3或者5得到的。
"""
class Solution:
	def GetUglyNumber_Solution(self,index):
		if index<7:
			return index
		res=[1,2,3,4,5,6]
		t2,t3,t5=3,2,1
		for i in range(6,index):
			res.append(min(res[t2]*2, min(res[t3]*3, res[t5]*5)))
			while res[t2]*2<=res[i]:
				t2+=1
			while res[t3]*3<=res[i]:
				t3+=1
			while res[t5]*5<=res[i]:
				t5+=1	
		return res[index-1]

S=Solution()
print(S.GetUglyNumber_Solution(100))