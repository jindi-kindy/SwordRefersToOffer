"""
题目:
统计一个数字在排序数组中出现的次数
可以运用二分查找法
"""
class Solution:
	#二分查找法找到k 值的位置
	def BinarySearch(self,data,mlen,k):
		start=0
		end=mlen-1
		while start<=end:
			mid=(end+start)//2
			if data[mid]<k:
				start=mid+1
			elif data[mid]>k:
				end=mid-1
			else:
				return mid
		return -1

	def GetNumberOfK(self,data,k):
		mlen=len(data)
		index=self.BinarySearch(data, mlen, k)
		if index==-1:
			return 0

		count=1
		for i in range(1,mlen):
			if index+i<mlen and data[index+i]==k:
				count+=1
			if index-i>=0 and data[index-i]==k:
				count+=1
		return count

S=Solution()
count=S.GetNumberOfK([1,2,3,3,3,6,7,8,9], 6)
print(count)