class Solution:
    def isHappy(self, n: int) -> bool:
        dict_steps_happy_number = {}
        while(True):
            n = step_happy_number(n)
            print(n)
            if n == 1:
                return True
            if n not in dict_steps_happy_number:
                dict_steps_happy_number[n] = 1
            else:
                return False

def step_happy_number(n):
    return sum(map(lambda x: x * x, map(int, str(n))))