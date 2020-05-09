# https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.store = list()
        
    def addNum(self, num: int) -> None:
        if not self.store:
            self.store.append(num)
        else:
            bisect.insort(self.store, num)

    def findMedian(self) -> float:
        n = len(self.store)
        
        if n % 2 == 1:
            return self.store[n // 2]
        else:
            return (self.store[n // 2 - 1] + self.store[n // 2]) * 0.5