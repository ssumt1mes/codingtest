T = int(input())
dp = [0,1,1,1,2,2,3,4,5,7,9]
for i in range(11,101,1) :
    num = dp[i-1]+dp[i-5]
    dp.append(num)
for _ in range(T) :
    N = int(input())
    print(dp[N])