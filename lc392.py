class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lastLine = [True for i in range(len(t)+1)]
        
        for i in range(len(s)):
            newLine = [False for _ in range(len(t)+1)]

            for j in range(len(t)):
                newLine[j+1]=newLine[j] or (lastLine[j] and s[i]==t[j])
                
            lastLine = newLine
            
        return lastLine[-1]
