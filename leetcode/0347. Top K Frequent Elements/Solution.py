# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        t = [(-count, num) for num, count in counts.items()]
        heapq.heapify(t)
        
        return [heapq.heappop(t)[1] for _ in range(k)]