# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        r = 0
        left, right = 0, len(height) - 1
        lmax, rmax = 0, 0
        
        while left < right:
            if height[left] > lmax:
                lmax = height[left]
            if height[right] > rmax:
                rmax = height[right]
            if lmax < rmax:
                r += max(0, lmax - height[left])
                left += 1
            else:
                r += max(0, rmax - height[right])
                right -= 1
                
        return r