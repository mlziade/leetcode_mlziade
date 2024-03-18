#Use a dictionary with a [key]value of [letters]num_of_occurency
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_magazine_letters = {}
        for i, letter in enumerate(magazine):
            if letter not in dict_magazine_letters:
                dict_magazine_letters[letter] = 1
            else:
                dict_magazine_letters[letter] += 1
        for i, ransom_letter in enumerate(ransomNote):
            if ransom_letter not in dict_magazine_letters:
                return False
            else:
                if dict_magazine_letters[ransom_letter] < 1:
                    return False
                else:
                    dict_magazine_letters[ransom_letter] -= 1
        return True

#Counter creates a dictionary of hashable objects with a counter of occoruncy (https://www.geeksforgeeks.org/python-counter-objects-elements/)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False