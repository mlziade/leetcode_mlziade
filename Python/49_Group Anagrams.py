from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_words = defaultdict(list)
        for words in strs:
            key = list(words)
            key.sort()
            dict_words["".join(key)] += [words]
        print(dict_words.values())
        return(dict_words.values())