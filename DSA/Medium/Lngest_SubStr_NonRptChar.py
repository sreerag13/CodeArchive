class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=[]
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if len(set(s[i:j])) == len(s[i:j]):
                    result.append(len(s[i:j]))
        lngChar=max(result,key=len)
        return len(lngChar)
    
if __name__=="__main__":
    