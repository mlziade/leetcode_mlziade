class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        list_n = list(str(x))
        list_n_rev = list(str(x))
        list_n_rev.reverse()
        print(list_n, list_n_rev)
        if list_n == list_n_rev:
            return True
        else:
            return False