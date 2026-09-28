class Solution:
    def maxDepth(self, s: str) -> int:
        dp=0
        r=0
        for ch in s:
            if ch==')':
                dp-=1
                continue
            if ch!='(':
                continue
            dp+=1
            if dp>r:
                r=dp
        return r
        