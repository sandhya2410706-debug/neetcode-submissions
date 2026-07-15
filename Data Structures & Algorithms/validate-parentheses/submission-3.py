class Solution:
    def isValid(self, s: str) -> bool:
        dict={'(':')',
                '{':'}',
                '[':']'}
        stack=[]
        for i in range(len(s)):
            
            if(s[i] in dict):
                stack.append(s[i])
            
            else :
                if(not stack):
                    return False
                top=stack.pop()
                if(dict[top]!=s[i]):
                    return False
        if not stack:
            return True
        else:
            return False


                


                

