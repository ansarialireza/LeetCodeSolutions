class KthLargest:

    def __init__(self, k:int, nums:list):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]
        


# Advanced

# import heapq
# from typing import List

# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.min_heap = nums
#         heapq.heapify(self.min_heap)
#         while len(self.min_heap) > k:
#             heapq.heappop(self.min_heap)

#     def add(self, val: int) -> int:
#         heapq.heappush(self.min_heap, val)
#         if len(self.min_heap) > self.k:
#             heapq.heappop(self.min_heap)
#         return self.min_heap[0]
