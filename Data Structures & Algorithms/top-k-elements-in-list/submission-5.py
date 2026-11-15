class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        min_freq = []
        for num, freq in counts.items():
            if len(min_freq) < k:
                heapq.heappush(min_freq, (freq, num))
            else:
                heapq.heappushpop(min_freq, (freq, num))
        
        elements = []
        for pair in min_freq:
            elements.append(pair[1])
        
        return elements