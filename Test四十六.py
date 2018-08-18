"""
题目:
孩子们的游戏，找到最终获得礼品的孩子编号
思路:

使用动态规划。我们注意到，输入的序列在删除一个元素后，序列的长度会改变，如果索引
在被删除的元素位置开始计算，那么每删除一个元素，序列的长度减一而索引会完全改变。
如果能找到改变前的索引和新索引的对应关系，那么该问题就容易解决了。
我们定义一个函数f(n, m)，表示每次在n个数字0,1,2,3,…,n-1中每次删除第m个数字后剩下
的数字。那么第一个被删除的数字的索引是(m-1)%n。删除该索引元素后，剩下的n-1个数字
为0,1,2,…,k-1,k+1,…,n-1。下次删除数字是重k+1位置开始，于是可以把序列看
作k+1,..,n-1,0,1,…,k-1。该序列最后剩下的序列也是f的函数。但该函数和第一个函数
不同，存在映射关系，使用f'来表示，于是有：f(n, m)=f'(n-1, m)。接下来需要找到映射关系。
k+1 --> 0
k+2 --> 1
     .
     .
     .
n-1 --> n-k-2
0   --> n-k-1
     .
     .
     .
k-1 --> n-2
所以可以得到：right = left-k-1，则p(x) = (x-k-1)%n，而逆映射是p'(x) = (x+k+1)%n
即0~n-1序列中最后剩下的数字等于（0~n-2序列中最后剩下的数字+k）%n，很明显当n=1时，
只有一个数，那么剩下的数字就是0.问题转化为动态规划问题，关系表示为：
 
    f(n)=(f(n-1)+m)%n； 当n=1,f(1)=0;
"""
class Solution:
	def LastRemaining_Solution(self,m,n):
		if n<1 or m<1:
			return -1
		last=0
		for i in range(2,n+1):
			last=(last+m)%i
		return last


"""
思路:
使用list模拟循环链表，用cur作为指向list的下标位置
当cur移到list末尾直接指向list头部，当删除一个数后list的长度和cur的值相等cur指向0
"""
class Solution1:
	def LastRemaining_Solution(self,m,n):
		if n<1 or m<1:
			return 
		childNum=list(range(n))
		#print(childNum)
		cur=0
		while len(childNum)>1:
			for i in range(1,m):
				cur+=1
				if cur==len(childNum):
					cur=0

			childNum.remove(childNum[cur])
			if cur==len(childNum):
				cur=0
		return childNum


S=Solution()
last=S.LastRemaining_Solution(3, 100)
print(last)

S=Solution1()
last1=S.LastRemaining_Solution(3, 100)
print(last1[0])