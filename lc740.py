class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        points = [0 for _ in range(max(nums)+1)]
        
        for num in nums:
            points[num]+=num
            
        points[1] = 1*points[1]
        
        for i in range(2, len(points)):
            points[i] = max(points[i]+points[i-2], points[i-1])
                
        return points[-1]
            