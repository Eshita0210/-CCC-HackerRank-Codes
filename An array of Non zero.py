n = int(input())
a = list(map(int, input().split()))

dp = [0] * n
dp2 = [0] * n

dp[0] = a[0]
dp2[0] = 0

for i in range(1, n):
    dp[i] = dp2[i-1] + a[i]
    dp2[i] = max(dp[i-1], dp2[i-1])

print(max(dp[-1], dp2[-1]))
