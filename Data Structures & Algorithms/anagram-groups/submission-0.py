class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # visited = [False] * len(strs)  # Track processed strings
        # result = []

        # for i in range(len(strs)):
        #     if visited[i]:
        #         continue  # Skip if already grouped

        #     group = [strs[i]]
        #     visited[i] = True

        #     for j in range(i + 1, len(strs)):
        #         # Check if strs[i] and strs[j] are anagrams
        #         if sorted(strs[i]) == sorted(strs[j]):
        #             group.append(strs[j])
        #             visited[j] = True

        #     result.append(group)

        # return result




        # Solution 2 --> T.C = O(n*(k log k)) 
        # using normal dictionary
        # group_map = {}

        # for word in strs:
        #     key = "".join(sorted(word))
        #     if key not in group_map:
        #         group_map[key] = []
        #     group_map[key].append(word)
        # return list(group_map.values())

        # using defaultdict
        # group_map = defaultdict(list)

        # for word in strs:
        #     key = "".join(sorted(word))
        #     group_map[key].append(word)
        # return list(group_map.values())



        # Solution - 3 -> T.C = O(n*k)
        group_map = {}
        for word in strs:
            cnt = [0] * 26

            for s in word:
                cnt[ord(s) - ord('a')] += 1

            # Convert list to tuple (because lists can't be dict keys)
            key = tuple(cnt)
            if key not in group_map:
                group_map[key] = []
            group_map[key].append(word)

        return list(group_map.values())
