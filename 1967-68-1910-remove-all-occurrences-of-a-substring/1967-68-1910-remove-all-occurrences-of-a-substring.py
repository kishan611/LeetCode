class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st = []
        x = len(part)
        for i in s:
            st.append(i)
            if st[-1]==part[-1]:
                if "".join(st[-x:])==part:
                    for j in range(x):
                        st.pop()
        return "".join(st)
        