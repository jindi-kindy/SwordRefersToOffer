
import math


def NumberOf1Between1AndN_Solution(n,x):
	if n<0 or x<1 or x>9:
		return 0
	i=1
	high=n
	total=0
	while high!=0:
		high=n//math.pow(10, i)
		tmp=n%math.pow(10, i)
		curr=tmp//math.pow(10,i-1)
		low=tmp%math.pow(10, i-1)
		if curr==x:
			total+=high*math.pow(10, i-1)+low+1
		elif curr<x:
			total+=high*math.pow(10, i-1)
		else:
			total+=(high+1)*math.pow(10, i-1)
		i+=1
	return total
total=NumberOf1Between1AndN_Solution(2593, 5)
print(total)