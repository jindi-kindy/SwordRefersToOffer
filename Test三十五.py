"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 
即输出P%1000000007
"""
import time
class Solution:
    def InversePairs(self, nums):
        # write code here
        def sortandcount(l, r):
            if r - l <= 1:
                return 0
            mid = (l + r)>>1
            count = sortandcount(l,mid) + sortandcount(mid, r)
            j = mid
            for i in range(l, mid):
                while j < r and nums[j] < nums[i]:
                    j += 1
                count += j - mid
            nums[l:r] = sorted(nums[l:r])
            return count%1000000007
        return (sortandcount(0,len(nums)))

S=Solution()
count=S.InversePairs([1,2,3,4,5,6,1])
print(count)


