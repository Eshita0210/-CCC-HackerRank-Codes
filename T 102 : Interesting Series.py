F0, F1, F2, N = map(int, input().split())

dp = [0] * (N + 1)
dp[0], dp[1], dp[2] = F0, F1, F2

for i in range(3, N+1):
    dp[i] = dp[i-1] ^ dp[i-2] + dp[i-3]

print(dp[N])
