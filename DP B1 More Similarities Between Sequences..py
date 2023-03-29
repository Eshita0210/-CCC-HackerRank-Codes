n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# create a matrix to store the lengths of the longest common subsequence
# between prefixes of the sequences
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# the length of the longest common subsequence is the maximum value in the matrix
k = dp[n][m]

print(k)
