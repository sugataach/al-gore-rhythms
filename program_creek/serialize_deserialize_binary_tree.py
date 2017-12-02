import json

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    def tuplify(root):
        return root and (root.val, tuplify(root.left), tuplify(root.right))
    return json.dumps(tuplify(root))

def deserialize(data):
    def detuplify(t):
        if t:
            root = TreeNode(t[0])
            root.left = detuplify(t[1])
            root.right = detuplify(t[2])
            return root
    return detuplify(json.loads(data))

root = TreeNode(1,TreeNode(2),TreeNode(3))
print(serialize(root))
data = '[1, [2, null, null], [3, null, null]]'
print(deserialize(data).left.val)
