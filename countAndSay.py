# Question Source : https://leetcode.com/problems/count-and-say/

def cas(n) :
    if n == 1 :
        return 1
    else :
        string = "" + str(1)
        
        for i in range(1,n):
            slen=len(string)
            k=0
            prev=0
            counter=0 
            result = ""
            while k<slen :
                if k==0 :
                    prev = string[k]
                if prev == string[k] :
                    counter+=1
                if prev != string[k] :
                    result = result + str(counter) + prev 
                    counter = 1
                    prev = string[k]      
                if k == slen-1 :
                    result = result + str(counter) + prev      
                k+=1
            string = result
        # print(string)
        return string


# print(cas(1))
print(cas(7))