class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for i,ch in enumerate(s,1):
            rev=26-(ord(ch)-ord('a'))
            res+=rev*i
        return res
        