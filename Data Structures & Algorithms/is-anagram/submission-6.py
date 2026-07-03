class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
    ans=False
    s="".join(sorted(s))
    t="".join(sorted(t))
    if(s==t):
        ans=True
    return ans



    
                