class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result=[]
        while listNode:
            result.insert(0,listNode.val)
            listNode=listNode.next
        return result