class TreeNode:
    def __init__(self , val = 0 , left = None , right = None ):
        self.val = val
        self.left = left
        self.right = right


def MergeTree(root1 , root2):

    if root1 is None:
        return root2
    if root2 is None:
        return root1

    root1.val += root2.val
    root1.left = MergeTree(root1.left , root2.left)
    root1.right = MergeTree(root1.right , root2.right)

    return root1.val


root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.left.left = TreeNode(5)
root1.right = TreeNode(2)


root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.left.right = TreeNode(4)
root2.right = TreeNode(3)
root2.right.right = TreeNode(7)

print(MergeTree(root1, root2))