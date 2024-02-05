class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        d1={}
        if(len(s)!=len(t)):
            return(False)
        for i in s:
            if i not in d:
                d[i]=1 
            else:
                d[i]+=1 
        for j in t:
            if j not in d1:
                d1[j]=1 
            else:
                d1[j]+=1
        for i in s:
            if i not in t:
                return(False)
            if(d[i]!=d1[i]):
                return(False)
        return(True)
