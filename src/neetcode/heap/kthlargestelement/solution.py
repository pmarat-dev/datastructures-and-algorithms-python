import heapq
from typing import List


class Solution:
    def __init__(self, k: int, nums: List[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


if __name__ == "__main__":
    solution = Solution(3, [1, 2, 5, 7])
    print(solution.add(4))
    print(solution.add(9))
