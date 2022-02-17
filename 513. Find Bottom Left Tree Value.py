


class TreeNode:
    def __init__(self , val  = 0 , left = None , right  = None):
        self.val = val
        self.left = left
        self.right = right


def bfsForTree(root):

    global res
    if root is None:
        return None

    queue = [root]

    while queue:
        node = queue.pop(0)
        res = node.val

        if node.right :
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return res



root = TreeNode(1)
root.left = TreeNode(2)
root.left.left  = TreeNode(4)
root.right = TreeNode(3)
root.right.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.left.left = TreeNode(7)


print(bfsForTree(root))