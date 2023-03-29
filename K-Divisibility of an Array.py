n, k = map(int, input().split())
a = list(map(int, input().split()))

rem_counts = [0] * k
for x in a:
    rem_counts[x % k] += 1

ans = 0
for i in range(1, (k+1)//2):
    ans += rem_counts[i] * rem_counts[k-i]

if k % 2 == 0:
    ans += (rem_counts[k//2] * (rem_counts[k//2] - 1)) // 2

ans += (rem_counts[0] * (rem_counts[0] - 1)) // 2

print(ans)
