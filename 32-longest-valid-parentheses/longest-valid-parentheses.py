class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        ans=0
        for i,val in enumerate(s):
            if val=='(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    ans=max(ans,i-st[-1])
        return ans
        