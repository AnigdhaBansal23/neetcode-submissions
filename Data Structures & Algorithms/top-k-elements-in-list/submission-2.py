import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap = []

        # freq = {}
        # for i in nums:
        #     freq[i] = freq.get(i,0) + 1
        
        # for num,count in freq.items():
        #     heapq.heappush(heap, (count,num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return [num for count,num in heap]
        
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1

        bucket_arr = [[] for i in range(len(nums) + 1)]
        for num,count in freq.items():
            bucket_arr[count].append(num)
        
        result = []
        for i in range(len(bucket_arr) - 1, 0, -1):
            for j in range(len(bucket_arr[i])):
                result.append(bucket_arr[i][j])
                if len(result) == k:
                    return result






        
