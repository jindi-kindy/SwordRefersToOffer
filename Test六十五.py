"""
题目:
设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径，路径可以从矩阵中的任意一个格子开始，
每一步可以在矩阵中向四个方向移动一个格子，如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子
"""
class Solution:
    def hasPath(self,s,rows,cols,path):
        if not s or not s[0] or not path:
            return False
        matrix=[[''for j in range(cols)] for i in range(rows)]
        count=0
        for i in range(rows):
            for j in range(cols):
                matrix[i][j]=s[count]
                count+=1
        def dfs(matrix,i,j,s):
            if not s:
                return True
            if i  <0 or i>=rows or j<0 or j>=cols:
                return False
            if matrix[i][j]!=s[0]:
                return False
            tmp=matrix[i][j]
            matrix[i][j]='#'
            res=dfs(matrix,i-1,j,s[1:]) or dfs(matrix,i+1,j,s[1:]) or dfs(matrix,i,j-1,s[1:]) or dfs(matrix,i,j+1,s[1:])
            matrix[i][j]=tmp
            return res
        for i in range(0,rows,1):
            for j in range(0,cols,1):
                if matrix[i][j]==path[0]:
                    if dfs(matrix,i,j,path):
                        return True
        return False

S=Solution()
s=['a','b','c','e','s','f','c','s','a','d','e','e']
rows=3
cols=4
path=''
flag=S.hasPath(s,rows,cols,path)
print(flag)