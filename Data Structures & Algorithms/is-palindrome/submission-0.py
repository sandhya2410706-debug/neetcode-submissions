class Solution:
    def isPalindrome(self, s: str) -> bool:
       result=re.sub('[^a-zA-Z0-9]','',s)
       n=len(result)-1
       result=result.lower()
       for i in range(len(result)):
            if(result[i]!=result[n-i]):
                return False
       return True
