s = "programming"

def first_repeating_char(s):
    s1 = [0]* 256

    for i in range(len(s)):
        s1[ord(s[i])] += 1

    for i in range(len(s)):
        if(s1[ord(s[i])] == 2):
            return s[i]

        
ans = first_repeating_char(s)
print(ans)
