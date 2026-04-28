class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # cnt_s = Counter(s)
        # cnt_t = Counter(t)
        # return cnt_s == cnt_t
        if len(s) != len(t):
            return False
        
        # count_s = {}
        # count_t = {}
        # for i in s:
        #     count_s[i] = count_s.get(i,0)+1
        # for i in t:
        #     count_t[i] = count_t.get(i,0)+1
        # return count_s == count_t

        # count = {}
        # for i in s:
        #     count[i] = count.get(i,0) + 1
        # for i in t:
        #     if i not in count or count[i] == 0:
        #         return False
        #     else:
        #         count[i] -= 1
        # return True
            
        # count_s = {}
        # for i in s:
        #     if i in count_s:
        #         count_s[i] += 1
        #     else:
        #         count_s[i] = 1
        # count_t = {}
        # for i in t:
        #     count_t[i] = count_t.get(i,0) + 1
        # return count_s == count_t

        # count = {}
        # for i in range(len(s)):
        #     count[s[i]] = count.get(s[i],0) + 1
        #     count[t[i]] = count.get(t[i],0) - 1
        # for key,value in count.items():
        #     if value != 0:
        #         return False
        # return True

        count = [0] * 26
        for i in s:
            count[ord(i) - ord('a')] += 1
        for i in t:
            count[ord(i) - ord('a')] -= 1
        return all(x == 0 for x in count)