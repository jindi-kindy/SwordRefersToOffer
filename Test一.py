"""在一个二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。"""

def Find(target,array):
	rows=len(array)
	cols=len(array[0])
	if rows>0 and cols>0:
		row=0
		col=cols-1
		while row<rows and col>=0:
			if target==array[row][col]:
				return True
			elif target>array[row][col]:
				row+=1
			else:
				col-=1
	return False

if __name__=='__main__':
	array=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
	flag=Find(7, array)
	print(flag)