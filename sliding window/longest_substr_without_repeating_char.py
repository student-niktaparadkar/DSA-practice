s = "abcabcbb"

def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}

        max_len = float('-inf')

        left =0
        right =0

        while(right<len(s)):
            if(s[right] in dict):
                dict[s[right]] += 1

            else:
                dict[s[right]] = 1

            while(dict[s[right]] >1):

                dict[s[left]] -= 1

                if(dict[s[left]]==0):
                    del dict[s[left]]

                left += 1

            max_len = max(max_len,right-left+1)
            right += 1

        if(s==""):
            return 0

        return max_len
