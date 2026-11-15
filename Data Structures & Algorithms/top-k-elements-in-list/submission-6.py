class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        min_freq = []
        for num, freq in counts.items():
            if len(min_freq) < k:
                heapq.heappush(min_freq, (freq, num))
            else:
                heapq.heappushpop(min_freq, (freq, num))
        
        return [num for freq, num in min_freq]