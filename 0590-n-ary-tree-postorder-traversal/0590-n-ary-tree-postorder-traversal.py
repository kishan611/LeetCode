"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        if not root:
            return res
        s=[root]
        while s:
            vertex=s.pop()
            if vertex.children:
                s.append(vertex)
                for i in vertex.children[::-1]:
                    s.append(i)
                vertex.children=[]
            else:
                res.append(vertex.val)
        return res
            
        
        
        