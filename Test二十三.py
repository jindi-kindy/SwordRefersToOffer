"""
题目:
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果
思路:
后序遍历的序列中，最后一个数字是树的根节点，数组中前面的数字可以分为两部分，
第一部分是左子树节点的值，都比根节点的值小，第二部分是右子树节点的值,都比根节点的值
大，后面用递归分别判断前后两部分是否符合以上原则
"""
class Solution:
	def VerifySquenceOfBST(self,sequence):
		if sequence==None or len(sequence)==0:
			return False
		length=len(sequence)
		root=sequence[length-1]
		for i in range(length):
			if sequence[i]>root:
				break
		for j in range(i,length):
			if sequence[j]<root:
				return False
		left=True
		if i>0:
			left=self.VerifySquenceOfBST(sequence[0:i])
		right=True
		if i<length-1:
			right=self.VerifySquenceOfBST(sequence[i:-1])
		return left and right

S=Solution()
flag=S.VerifySquenceOfBST([5,7,6,9,11,10,8])
print(flag)