class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        mF = []
        for num in counts.keys():
            if len(mF) < k:
                heapq.heappush(mF, (counts[num], num))
            else:
                heapq.heappushpop(mF, (counts[num], num))
        
        elements = []
        for pair in mF:
            elements.append(pair[1])
        
        return elements