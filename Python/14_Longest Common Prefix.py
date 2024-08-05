class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        sizes_arr = list(map(len_str, strs))
        final_str = ""
        for i in range(max(sizes_arr)):
            primeiros = [ return_char_pos(strs[j], i) for j in range(len(strs)) ]
            print(primeiros)
            if primeiros.count(primeiros[0]) != len(strs):
                return final_str
            final_str += primeiros[0]
            print(final_str)
        return "" if final_str == "" else final_str


def len_str(n):
    return len(n)

def return_char_pos(n, i):
    try:
        return str(n)[i]
    except:
        return ""