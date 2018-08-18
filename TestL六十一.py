"""
题目:
实现两个函数，分别用来序列化和反序列化二叉树
思路:
序列化部分，按行，如果为空，就用'.'代替，最后序列化的结果用一个list保存
反序列化部分，递归，增加一个idx变量，指示位置
"""

class TreeLinkNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def Serialize(self,root):
        if root==None:
            return ["."]
        nodes_list=[[root]]
        result=[]
        while nodes_list:
            current_nodes=nodes_list[0]
            nodes_list=nodes_list[1:]
            new_nodes=[]
            flag=False
            for node in current_nodes:
                if node!=None:
                    flag=True
                    break
            if flag!=True:
                return result
            while current_nodes:
                if current_nodes[0]!=None:
                    result.append(current_nodes[0].val)
                    new_nodes.append(current_nodes[0].left)
                    new_nodes.append(current_nodes[0].right)
                else:
                    result.append('.')
                    new_nodes.append(None)
                    new_nodes.append(None)
                current_nodes=current_nodes[1:]
            if new_nodes:
                nodes_list.append(new_nodes)
        return result

    def Deserialize(self, s, idx=0):
        if idx >= len(s):
            return None
        if s[idx] == '.':
            return None
        root = TreeLinkNode(int(s[idx]))
        root.left = self.Deserialize(s, idx * 2 + 1)
        root.right = self.Deserialize(s, idx * 2 + 2)
        return root



T=TreeLinkNode(1)
T.left=TreeLinkNode(2)
T.right=TreeLinkNode(3)
#T.left.left=TreeLinkNode(4)
T.left.right=TreeLinkNode(5)
T.right.left=TreeLinkNode(6)
T.right.right=TreeLinkNode(7)
#T.left.left.left=TreeLinkNode(8)

S=Solution()
s=S.Serialize(T)
root=S.Deserialize(s)
print(s)
print(root)