class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res=[folder[0]]
        for i in folder[1::]:
            l=res[-1]+"/"
            if i[:len(l)]!=l:
                res.append(i)
        return res