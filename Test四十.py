"""
题目:
一个整型数组里除了两个数字之外，其他的数字都出现了两次
思路:
由于两个数字肯定不一样，那么异或的结肯定不为0，也就是说这个结果数组的二进制
表示至少有一个位为1，我们在结果数组中找到第一个为1的位的位置，记为第n位，现在以
第n位是不是1为标准把元组中的数字分成两个子数组。
"""


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        ans=0
        for x in array:
        	ans=ans^x
        flag=len(bin(ans))-bin(ans).index('1')
        list1=[]
        list2=[]
        for x in array:
        	if bin(x)[-flag]=='1':
        		list1.append(x)
        	else:
        		list2.append(x)
       	ans1=0;ans2=0
       	for x in list1:
       		ans1=ans1^x
       	for x in list2:
       		ans2=ans2^x
       	return [ans1,ans2]

S=Solution()
print(S.FindNumsAppearOnce([2,4,3,6,3,2,5,5]))
