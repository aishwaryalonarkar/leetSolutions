# Implement strStr()
# Question Source = https://leetcode.com/problems/implement-strstr/

def getIndex(haystack,needle) :
    haySize = len(haystack)
    nSize = len(needle)
    isAt = -1
    if haySize < nSize or haySize < 1 :
        return -1
    if nSize == 0 :
        return 0
    for i in range(0,haySize-nSize) :
        if haystack[i] == needle[0] and haystack[i+nSize-1] == needle[-1] and haystack[i:i+nSize] == needle :
            isAt = i
            break
    return isAt

            


haystack = "hakelopopo"
needle = "kel"
print(getIndex(haystack,needle))

haystack = "aaaaa"
needle = "bba"
print(getIndex(haystack,needle))
