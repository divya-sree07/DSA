class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap={}
        if len(s)!=len(t):
            return False
        for i in t:
            if i in hashMap:
                hashMap[i]=hashMap[i]+1
            else:
                hashMap[i]=1
        for i in s:
            if i in hashMap:
                hashMap[i]=hashMap[i]-1
            else:
                return False
        for i in hashMap:
            if hashMap[i]!=0:
                return False
        return True


        