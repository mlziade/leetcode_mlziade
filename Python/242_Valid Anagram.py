class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if not s or not t:
            return False
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        for i,j in zip(s,t):
            dict_s[i] += 1
            dict_t[j] += 1
        for [key,value] in dict_s.items():
            if value != dict_t[key]:
                return False
        return True
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if not s or not t:
            return False
        dict_ = defaultdict(int)
        for i,j in zip(s,t):
            dict_[i] += 1
            dict_[j] -= 1
        for val in dict_.values():
            if val != 0:
                return False
        return True