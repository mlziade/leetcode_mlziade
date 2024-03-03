class Solution:
    def reverse(self, x: int) -> int:
        aux_num = x if x > 0 else -x
        reversed_num = 0
        while(aux_num >= 1):
            last_digit = aux_num % 10
            reversed_num = (reversed_num * 10) + last_digit
            aux_num = (aux_num) // 10
            print(aux_num, reversed_num)
        reversed_num = reversed_num if x > 0 else -reversed_num
        if -2147483648 > reversed_num or reversed_num > 2147483647:
            return 0
        return reversed_num
