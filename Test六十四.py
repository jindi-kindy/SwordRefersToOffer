"""
题目:
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}
"""
class Solution:
    def maxInWindows(self, num, size):
        n=len(num)
        if num==[]:
            return []
        smallnum=[]
        maxlist=[]
        if n>=size and size>0:
            for i in range(n-size+1):
                smallnum=num[i:i+size]
                maxlist.append(max(smallnum))
            return maxlist
        else:
            return []

S=Solution()
result=S.maxInWindows([2,3,4,2,6,2,5,1],3)
print(result)