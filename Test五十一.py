"""
题目:
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
思路:
把B[i]=A[0]*A[1]*...A[n-1],看成A[0]*A[1]*...A[i-1]和A[i+1]*...A[n-2]*A[n-1]两部分乘积
"""
class Solution:
    def multiply(self,A):
        head=[1]
        tail=[1]
        for i in range(len(A)-1):
            head.append(head[i]*A[i])
            tail.append(tail[i]*A[-i-1])
        B=[]
        for i in range(len(A)):
            B.append(head[i]*tail[-i-1])
        return B

S=Solution()
B=S.multiply([1,2,3,4,5])
print(B)