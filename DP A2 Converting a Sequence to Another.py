n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# Initialize dp table
dp = [[0]*(m+1) for _ in range(n+1)]

# Base case
for i in range(n+1):
    dp[i][0] = i
for j in range(m+1):
    dp[0][j] = j

# Fill dp table
for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

# Print result
print(dp[n][m])
