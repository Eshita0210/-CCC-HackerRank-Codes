def F(A, B):
    n = len(A)
    m = len(B)
    dp = [[0] * (m+1) for _ in range(n+1)]
    result = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > result:
                    result = dp[i][j]
    return result

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

print(F(A, B))
