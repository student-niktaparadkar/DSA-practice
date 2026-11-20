s1 = "listen"
s2 = "silent"

def check_anagram_str(s1,s2):
    if(len(s1) != len(s2)):
        return False
    
    freq = [0]*256

    for i in range(len(s1)):
        freq[ord(s1[i])] += 1

    for i in range(len(s2)):
        freq[ord(s2[i])] -= 1

    for i in range(len(freq)):
        if(freq[i] != 0):
            return False

    return True

if(check_anagram_str(s1,s2)):
    print("str is anagram")

else:
    print("str is not anagram")
