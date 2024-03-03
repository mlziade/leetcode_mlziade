class Solution:
    def longestPalindrome(self, s: str) -> str:
        aux_max_sub = s[0]
        match len(s):
            case 1:
                return s
            case 2:
                if s[0] == s[1]:
                    return s
        max_Len= 1
        s_size = len(s) # 3 <= s_size <= 1000
        for i in range(s_size-1):
            for j in range(i+1, s_size): #Só comecar a partir de um tamanho maior que o len de aux_max_sub
                if j-i+1 > max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    max_Len = j-i+1
                    aux_max_sub = s[i:j+1]
        return aux_max_sub

                    
        
        