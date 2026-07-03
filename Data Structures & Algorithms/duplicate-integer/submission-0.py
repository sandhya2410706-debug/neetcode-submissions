class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        ans=False
        for i in (nums):
           if i in seen:
               ans=True
           else :
                seen.add(i)
        return ans

            


            
        