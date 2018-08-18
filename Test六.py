"""
把一个数组最开始的若干个元素搬到数组的末尾，称之为数组的旋转。输入一个非递减排序的数组的一个旋转，
输出旋转数组的最小元素，例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：
给出的所有元素都大于0，若数组大小为0，请返回0。
"""
class Solution:
	def minNumberInRotateArray(self,rotateArray):
		if len(rotateArray)==0:
			return 0
		left=0
		right=len(rotateArray)-1
		mid=0
		while rotateArray[left]>=rotateArray[right]:
			if right-left==1:
				mid=right
				break
			mid=left+(right - left)//2
			if rotateArray[left]==rotateArray[mid] and rotateArray[right]==rotateArray[mid]:
				return self.minInorder(rotateArray,left,right)
			if rotateArray[mid]>=rotateArray[left]:
				left=mid
			else:
				right=mid
		return rotateArray[mid]

	def minInorder(self,array,left,right):
		result=array[left]
		for i in range(left+1,right):
			if array[i] < result:
				result=array[i]
		return result

if __name__=='__main__':
	S=Solution()
	mid=S.minNumberInRotateArray([1,1,1,0,1])
	print(mid)