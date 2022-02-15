class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isUnivalTree(root):

    if root is None:
        return True
    if root.left :
        if root.val != root.left.val:
            return False
    if root.right :
        if root.val != root.right.val:
            return False
    return isUnivalTree(root.left) and isUnivalTree(root.right)

root = TreeNode(1)
root.left = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right = TreeNode(1)
root.right.right = TreeNode(1)


print(isUnivalTree(root))