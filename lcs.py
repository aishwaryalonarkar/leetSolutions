# Longest Common Subsequence

def getlcs(str1,str2) :
    s1 = len(str1)
    s2 = len(str2)

    dp = [[0 for x in range(s2+1)] for x in range(s1+1)]

    for i in range(len(dp)) :
        for j in range(len(dp[i])) :
            if i>0 and j>0 :
                if str1[i-1] == str2[j-1] :
                    dp[i][j] = dp[i-1][j-1] + 1
                else :
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    printdp(dp,str1,str2)

    # Backtracking 
    str = ""

    while i>0 and j>0 :
        if str1[i-1] == str2[j-1] :
            str = str1[i-1] + str
            i-=1
            j-=1
        elif dp[i-1][j] > dp[i][j-1] :
            i-=1
        else :
            j-=1
    print(str)


def printdp(dp,str1,str2) :
    print("    ", end = "  ")
    for i in str2 :
        print(i,end="  ")
    print(" ")
    for x,i in enumerate(dp) :
        if x==0 :
            print("",end="  ")
        if x>0 :
            print(str1[x-1],end = " ")
        print(i)

str1 = "acadb"
str2 = "cbda"
getlcs(str1,str2)