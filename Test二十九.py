"""
题目:
输入n个整数，找出其中最小的K个数
"""
def QuickSort(input_list,left,right,k):

	def division(input_list,left,right):
		base=input_list[left]
		while left<right:
			while left<right and input_list[right]>=base:
				right-=1
			input_list[left]=input_list[right]
			while left<right and input_list[left]<=base:
				left+=1
			input_list[right]=input_list[left]
		input_list[left]=base
		return left


	if left<right:
		base_index=division(input_list, left, right)	
		QuickSort(input_list, left, base_index-1,k)
		QuickSort(input_list, base_index+1, right,k)

	return (input_list[:k])
if __name__=='__main__':
	input_list=[6,4,8,9,2,3,1]
	s=QuickSort(input_list, 0, len(input_list)-1,2)
	print(s)
