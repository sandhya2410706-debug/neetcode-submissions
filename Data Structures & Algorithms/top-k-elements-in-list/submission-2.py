class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        ans=[]
        count=0
        for i in range(len(nums)):
            dict[nums[i]]=nums.count(nums[i])
            sorted(dict)
        while(k>0):
            m=max(dict,key=dict.get)
            ans.append(m)
            dict.pop(m)
            k-=1
            ans.sort()
        return ans


        