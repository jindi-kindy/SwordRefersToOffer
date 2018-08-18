"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
"""
class Solution():
	def printMatrix(self,matrix):
		rows=len(matrix)
		cols=len(matrix[0])
		result=[]
		if rows==0 and cols==0:
			return result
		left,right,top,bottom=0,cols-1,0,rows-1
		while left<=right and top<=bottom:
			for i in range(left,right+1):
				result.append(matrix[top][i])
			for i in range(top+1,bottom+1):
				result.append(matrix[i][right])
			if top!=bottom:
				for i in range(left,right)[::-1]:
					result.append(matrix[bottom][i])
			if left!=right:
				for i in range(top+1,bottom)[::-1]:
					result.append(matrix[i][left])
			left+=1
			right-=1
			top+=1
			bottom-=1
		return result

S=Solution()
result=S.printMatrix([[1,2,3,4],[5,6,7,8,],[9,10,11,12],[13,14,15,16]])
print(result)