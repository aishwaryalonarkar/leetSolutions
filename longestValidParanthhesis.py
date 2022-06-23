# Question Sourrce : https://leetcode.com/problems/longest-valid-parentheses/

def getLongest(s) :
    r=0
    l=0
    i=0
    maxLen = 0

    while i<len(s):
        if s[i] == "(":
            l+=1
        else :
            r+=1
        if r==l :
            maxLen = max(maxLen, l+r)
        elif r>= l :
            l=r=0
        i+=1

    i-=1
    while i>0:
        if s[i] == "(":
            l+=1
        else :
            r+=1
        if r==l :
            maxLen = max(maxLen, l+r)
        elif r<= l :
            l=r=0
        i-=1
    return maxLen

print(getLongest("))))()()))"))
