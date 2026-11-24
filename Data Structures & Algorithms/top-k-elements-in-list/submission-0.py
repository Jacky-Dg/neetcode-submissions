import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        mF = []
        for num in counts.keys():
            if len(mF) <= k or num > mF[0]:
                heapq.heappush(mF, num)

            if len(mF) > k:
                heapq.heappop(mF)
        
        return mF