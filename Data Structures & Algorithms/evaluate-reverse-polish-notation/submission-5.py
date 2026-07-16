class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ans=0
        for i in range(len(tokens)):
            if(tokens[i] not in['*','/','+','-']):
                stack.append(int(tokens[i]))
            else:
                top1=stack.pop()
                top2=stack.pop()

                if(tokens[i]=='/'):
                    stack.append(int(top2/top1))
                elif(tokens[i]=='*'):
                   stack.append(top2*top1)
                elif(tokens[i]=='+'):
                    stack.append(top2+top1)
                elif(tokens[i]=='-'):
                    stack.append(top2-top1)
        ans=stack.pop()
        return ans


