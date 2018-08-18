"""
连续子数组的最大和
"""
class Solution:

	def FindGreatestSumOfSubArray(self, array):
	        res =len(array) and max(array)
	        temp = 0
	        for i in array:
	            temp = max(i,temp+i)
	            res = max(res,temp)
	        return res

S=Solution()
res=S.FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5])
print(res)