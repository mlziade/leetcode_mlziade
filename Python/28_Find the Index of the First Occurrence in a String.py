class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size_h = len(haystack)
        size_n = len(needle)

        if size_h < size_n:
            return -1

        for i in range(size_h):
            if size_h < i + size_n:
                return -1
            
            n_aux = 0
            j = i
            
            while j < size_h and n_aux < size_n and haystack[j] == needle[n_aux]:
                j += 1
                n_aux += 1
                
            if n_aux == size_n:
                return i
                
            i += 1
        return -1
        