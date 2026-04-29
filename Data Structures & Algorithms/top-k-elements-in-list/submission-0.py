class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums)
        # return [num for num,freq in count.most_common(k)]


        # SOLUTION - 1 
        # T.C = O(nlogn)
        # freq = {}
        # for i in nums:
        #     freq[i] = freq.get(i,0) + 1
        
        # # sort dictionary based on their values
        # result = sorted(freq.keys(), key = lambda x : freq[x], reverse = True)
        # return result[:k]


        # SOLUTION-2
        # HEAP - top K -> always think of heap 
        # T.C -> Heap operations: O(log k);For all elements: O(n log k)
        # freq = {}
        # for i in nums:
        #     freq[i] = freq.get(i,0) + 1

        # heap = []
        # for num, count in freq.items():
        #     heapq.heappush(heap, (count,num))

        #     if(len(heap)) > k:
        #         heapq.heappop(heap)

        # return [num for count,num in heap]

        # SOLUTION - 3 -> BUCKET SORT 
        # T.C = Counting: O(n) | Bucket fill: O(n) | Traversal: O(n) | total = O(n)

        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        buckets = [[] for i in range(len(nums)+1)]
        for num,count in freq.items():
            buckets[count].append(num)
        
        # Collect top k elements
        res = []
        # Traverse from high freq → low
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
