n = int(input())
arr = list(map(int, input().split()))

max_right = 0
for i in range(n-1, -1, -1):
    current = arr[i]
    arr[i] = max_right
    max_right = max(max_right, current)

arr[n-1] = 0
print(*arr)
