class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        res=0
        for i,c in enumerate(s):
            if c==")":
                st.pop()
                if st:
                    res=max(res,i-st[-1])
                else:
                    st.append(i)
            else:
                st.append(i)
        return res