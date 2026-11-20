s = "abcdeefg"

def unique_char(s):

    s1 = [0]*256

    for i in range(len(s)):
        s1[ord(s[i])] += 1

    for i in range(len(s1)):
        if(s1[i] > 1):
            return False

    return True

if(unique_char(s)):
    print("str is unique")
else:
    print("str is not unique")
