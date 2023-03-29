n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
x, y, z = map(int, input().split())

# create a matrix to store the minimum cost of converting prefixes of A to prefixes of B
dp = [[0] * (m + 1) for _ in range(n + 1)]

# initialize the first row and column of the matrix with the cost of inserting/removing
# all elements in A or B up to that position
for i in range(n + 1):
    dp[i][0] = i * y
for j in range(m + 1):
    dp[0][j] = j * x

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            # compute the cost of the three possible operations and take the minimum
            insert_cost = dp[i][j - 1] + x
            remove_cost = dp[i - 1][j] + y
            modify_cost = dp[i - 1][j - 1] + z
            dp[i][j] = min(insert_cost, remove_cost, modify_cost)

# the minimum cost of converting A to B is stored in dp[n][m]
min_cost = dp[n][m]

print(min_cost)
