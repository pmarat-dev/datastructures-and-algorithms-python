import heapq
from typing import List


def last_stone_weight(stones: List[int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if second > first:
            heapq.heappush(stones, first - second)

    stones.append(0)
    return abs(stones[0])


if __name__ == "__main__":
    print(last_stone_weight([1, 4, 6, 9]))
