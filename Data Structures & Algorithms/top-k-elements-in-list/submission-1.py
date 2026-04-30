import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        for num,count in freq.items():
            heapq.heappush(heap, (count,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count,num in heap]
        