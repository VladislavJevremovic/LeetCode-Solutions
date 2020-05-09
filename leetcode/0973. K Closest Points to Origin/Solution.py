# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:K]

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []
        
        r = []
        
        pd = [((point[0] ** 2 + point[1] ** 2), point) for point in points]
        heapq.heapify(pd)
        
        for _ in range(K):
            p = heapq.heappop(pd)[1]
            r.append(p)
            
        return r