class TreeNode:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right


def countUnival(root):
    count =[]
    countNode(root ,count )
    return sum(count)

def countNode(root ,count):
    if root is None:
        return None
    l = (countNode(root.left,count))
    r = (countNode(root.right,count))
    #print(l , r)
    if l is False or r is False:
        return False
    if root.left is not None and root.val != root.left.val:
        return False
    if root.right is not None and root.val != root.right.val:
        return False
    count.append(1)
    #print(count )
    return True








root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.left.left  = TreeNode(5)
root.right.left.right = TreeNode(5)
root.right.right =  TreeNode(6)
root.right.right.right = TreeNode(7)
print(countUnival(root))
