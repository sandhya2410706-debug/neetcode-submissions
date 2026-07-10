class Solution:
    def maxArea(self, heights: List[int]) -> int:
      max_area=0
      for i in range(len(heights)):
        for j in range(i+1,len(heights)):
            distance=j-i
            if(min(heights[i],heights[j])*distance>max_area):
                max_area=min(heights[i],heights[j])*distance

      return max_area



            
            

            