class Solution:

    def encode(self, strs: List[str]) -> str:
        # think about use some special character as a separation between the words
        # But problem says it contains possible characters out of 256 valid ASCII
        '''
        If the input list is empty, return an empty string.
        Create an empty list to store the sizes of each string.
        For each string, append its length to the sizes list.
        Build a single string by:
        Writing all sizes separated by commas.
        Adding a '#' to mark the end of the size section.
        Appending all the actual strings in order.
        Return the final encoded string.
        '''
        # corner case
        if len(strs) == 0:
            return ''
        str_len = []
        for s in strs:
            str_len.append(len(s))

        encode_s = ','.join(map(str, str_len))
        encode_s += '#'
        encode_s += ''.join(strs)
        return encode_s


    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        len_list = list(map(int, s[0:s.index('#')].split(',')))
        content_s = s[s.index('#')+1:]

        result = []

        index = 0
        for i in len_list:
            result.append(content_s[index: index + i])
            index += i
        return result


