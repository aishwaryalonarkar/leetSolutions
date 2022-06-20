# Fibonacci Series using Dynamic Programming bottom up Approach
class Fibonacci :
    def __init__(self) :
        self.dp = []

    def fib(self,n) :
        for i in range(0,n+1) :
            self.dp.append(-1)

        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2,n+1):
            self.dp[i] = self.dp[i-2] + self.dp[i-1]
            # print(self.dp[i])
        
        return self.dp[n]

f = Fibonacci()
print(f.fib(5))
