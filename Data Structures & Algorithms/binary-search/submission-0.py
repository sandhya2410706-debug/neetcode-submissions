class Solution:
    def search(self, nums: List[int], target: int):# -> int:
       mid=int(len(nums)/2)
       i=0
       while(i<mid):
            if(nums[i]==target):
                return i
            else:
                i+=1

       while(mid<len(nums)):
            if(nums[mid]==target):
                return mid
            else:
                mid+=1

       return -1

        

           
