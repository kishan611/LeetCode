class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        for i in s:
            if i==")":
                res=""
                while st[-1]!="(":
                    res+=st.pop()
                st.pop()
                st+=list(res)
            else:
                st.append(i)
        return "".join(st)