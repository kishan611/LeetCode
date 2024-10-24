# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        l1=[root1]
        l2=[root2]
        while l1 and l2:
            temp1=[]
            temp2=[]
            while l1 and l2:
                n1=l1.pop()
                n2=l2.pop()
                if n1.val!=n2.val:
                    return False
                n1l=n1.left
                n1r=n1.right
                n2l=n2.left
                n2r=n2.right
                if n1l and n2l and n1r and n2r:
                    if n1l.val==n2r.val:
                        n2.left=n2r
                        n2.right=n2l
                    elif n1l.val!=n2l.val or n1r.val!=n2r.val:
                        return False
                elif (n1l and n2r and n1l.val==n2r.val) or (n1r and n2l and n1r.val==n2l.val):
                    n2.left=n2r
                    n2.right=n2l 
                elif n1l and n2l and n1l.val!=n2l.val:
                    return False
                elif n1r and n2r and n1r.val!=n2r.val:
                    return False
                if n1.left:
                    temp1.append(n1.left)
                    if not n2.left:
                        return False
                    temp2.append(n2.left)
                elif n2.left:
                    return False
                if n1.right:
                    temp1.append(n1.right)
                    if not n2.right:
                        return False
                    temp2.append(n2.right)
                elif n2.right:
                    return False
            l1=temp1[::]
            l2=temp2[::]
        if l1 or l2:
            return False
        return True
                
                

                
                


                    
