#时间复杂度为:O(n)

class TreeNode:
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None

def getLen(root):
    if(root == None):
        return 0
    length=0
    if(root.left and (root.left.val) > root.val):
        length=max(length,getLen(root.left)+1)
    if(root.right and (root.right.val) > root.val):
        length=max(length,getLen(root.right))
    return length

def getLongSubList(root):
  if(root == None):
      return 0
  length = getLen(root)
  if(root.left):
      length=max(length,getLongSubList(root.left)+1)
  if(root.right):
      length=max(length,getLongSubList(root.right)+1)
  return length+1

def reConstructBinaryTree(pre,tin):
	if len(pre)==0:
		return None
	elif len(pre)==1:
		return TreeNode(pre[0])
	else:
		root=TreeNode(pre[0])
		pos=tin.index(pre[0])
		root.left=reConstructBinaryTree(pre[1:pos+1], tin[:pos])
		root.right=reConstructBinaryTree(pre[pos+1:], tin[pos+1:])
	return root

if __name__=='__main__':
    root = reConstructBinaryTree([5,6,1,8,7,9,6], [1,6,8,5,9,7,6])
    print(getLongSubList(root))
