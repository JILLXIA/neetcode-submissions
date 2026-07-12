class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict_group = {} # "00100xxx": ['hat]

        def build_anagram_str(s: str) -> str:
            tmp_list = [0] * 26

            for i in range(len(s)):
                tmp_list[ord(s[i]) - ord('a')] += 1
            return str(tmp_list)

        for str_entry in strs:
            count_s = build_anagram_str(str_entry)

            if count_s not in dict_group:
                dict_group[count_s] = []
            dict_group[count_s].append(str_entry)
        return list(dict_group.values())