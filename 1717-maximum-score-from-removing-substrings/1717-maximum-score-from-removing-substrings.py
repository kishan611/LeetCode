class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        st=[]
        res=0
        if x>y:
            for i in s:
                if i=="a":
                    st.append(i)

                elif i=='b':
                    if st and st[-1]=='a':
                        st.pop()
                        res+=x
                    else:
                        st.append(i)
                else:
                    st2=[]
                    for j in st:
                        if j=='b':
                            st2.append(j)
                        elif st2:
                            res+=y
                            st2.pop()
                    st=[]
            st2=[]
            for j in st:
                if j=='b':
                    st2.append(j)
                elif st2:
                    res+=y
                    st2.pop()
        else:
            for i in s:
                if i=="b":
                    st.append(i)

                elif i=='a':
                    if st and st[-1]=='b':
                        st.pop()
                        res+=y
                    else:
                        st.append(i)
                else:
                    st2=[]
                    for j in st:
                        if j=='a':
                            st2.append(j)
                        elif st2:
                            res+=x
                            st2.pop()
                    st=[]
            st2=[]
            for j in st:
                if j=='a':
                    st2.append(j)
                elif st2:
                    res+=x
                    st2.pop()
        return res