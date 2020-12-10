class Solution:
    def lengthOfLongestSubstring(self, s: str):
        res = 0
        if (len(s)) == 0:
            return res
        elif s.isspace():
            res = 1
            return res
        else:
            ans_l = []
            idx = 0
            start_idx = 0
            str_list = list(s)
            start_idx = idx
            while (idx < len(str_list)):
                if (str_list[idx] in ans_l):
                    idx = start_idx + 1
                    start_idx += 1
                    ans_l = []
                ans_l.append(str_list[idx])
                if (len(ans_l) > res):
                    res = len(ans_l)
                idx += 1
            return res






