s = "aabbcccdeee"

def char_with_max_freq(s):
    freq = [0]*256

    for i in range(len(s)):
        freq[ord(s[i])] += 1

    max_freq = float('-inf')
    ans = ""
    for i in range(len(freq)):
        if(freq[i]> max_freq):
            max_freq = freq[i]
            ans = chr(i)

    return ans

ans = char_with_max_freq(s) 
print(ans)  
