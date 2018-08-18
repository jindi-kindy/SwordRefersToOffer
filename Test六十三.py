"""
题目:
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值
"""
class Solution:
    def __init__(self):
        self.arr=[]
    def Insert(self,num):
        self.arr.append(num)
        self.arr.sort()
    def GetMedian(self,pock):
        lenght=len(self.arr)
        if lenght%2==1:
            return self.arr[lenght//2]
        return (self.arr[lenght//2]+self.arr[lenght//2-1])/2.0

S=Solution()
a=[2,3,4,1,5,7,6,7,8,6,5,4,3]
for i in range(0,len(a)):
    S.Insert(a[i])
z=S.GetMedian(0)
print(z)