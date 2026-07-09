class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)-1
        nums.sort()
        for i in range(n):
            left=i+1
            right=n

            while left<right:
                total=nums[i]+nums[left]+nums[right]

                if(total<0):
                    left+=1
                elif(total>0):
                    right-=1
                else :
                    target=[nums[i],nums[left],nums[right]]

                    if(target not in ans):
                        ans.append(target)
                    left+=1
                    right-=1
        return ans
