class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        
        # cs, ct = {}, {}
        # for i in range(len(s)):
        #     cs[s[i]] = 1 + cs.get(s[i], 0)
        #     ct[t[i]] = 1 + ct.get(t[i], 0)  
        # return cs == ct

        # return sorted(s) == sorted(t)
        return Counter(s) == Counter(t)