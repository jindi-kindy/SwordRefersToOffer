"""
题目:
求1+2+3+...+n,要求不能使用乘法，for、while、if、else等关键字及条件判断语句
"""
class Solution:
	def Sum_Solution(self,n):
		ans=n
		#a and b,a为False,返回a,a为True,就返回b
		temp=ans and self.Sum_Solution(n-1)
		ans=ans+temp
		return ans

S=Solution()
ans=S.Sum_Solution(4)
print(ans)
