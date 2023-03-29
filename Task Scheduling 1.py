def solve():
    n = int(input())
    t = list(map(int, input().split()))
    p = list(map(int, input().split()))

    tasks = sorted(zip(t, p), key=lambda x: -x[1])
    total_profit = 0
    schedule = [False] * n

    for task in tasks:
        deadline, profit = task
        for i in range(min(n, deadline)-1, -1, -1):
            if not schedule[i]:
                schedule[i] = True
                total_profit += profit
                break

    print(total_profit)

t = int(input())
for _ in range(t):
    solve()
