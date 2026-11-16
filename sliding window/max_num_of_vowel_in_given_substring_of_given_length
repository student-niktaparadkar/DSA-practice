s = "abciiidef"
k = 3


def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0
        for i in range(k):
            if (s[i] in "aeiou"):
                max_vowels += 1

        curr_vowels = max_vowels
        for i in range(k,len(s)):
            if(s[i] in "aeiou"):
                curr_vowels += 1

            if(s[i-k] in "aeiou"):
                curr_vowels -= 1

            max_vowels = max(max_vowels,curr_vowels)

        
        return max_vowels
