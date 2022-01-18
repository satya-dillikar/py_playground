# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class BinaryTree:
    def __init__(self, data=None):
        self.root = data



class Solution:
    def isSameTree(self, p, q):
        
        if p == None :
            if q == None:
                return True
            else:
                return False
        else:
            if q == None:
                return False
            else:
                if p.val != q.val:
                    return False
                else:
                    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
        return False

    def inOrderTravel(self,data,result):
        root = data
        if root != None:
            self.inOrderTravel(root.left,result)
            result.append(root.val)
            self.inOrderTravel(root.right,result)

    def inOrderTravelOutput(self,data):
        result =[]
        self.inOrderTravel(data,result)
        return result

# n1 =TreeNode(1)
# n2 =TreeNode(2)
# n3 =TreeNode(3)
# p = n1
# p.left = n2
# p.right = n3

# n1 =TreeNode(1)
# n2 =TreeNode(2)
# n3 =TreeNode(3)
# q = n1
# q.left = n2
# q.right = n3

# n1 =TreeNode(1)
# n2 =TreeNode(2)
# p = n1
# p.left = n2
# p.right = None

# n1 =TreeNode(1)
# n2 =TreeNode(2)
# q = n1
# q.left = None
# q.right = n2

s = Solution()
# isSame = s.isSameTree(p,q)
# print(isSame)

n1 =TreeNode(1)
n2 =TreeNode(2)
n3 =TreeNode(3)
n1.right = n2
n2.left = n3

tree = BinaryTree(n1)

result = s.inOrderTravelOutput(tree.root)
print(result)