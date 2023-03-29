n, m = map(int, input().split())

adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

head = int(input())

# Perform DFS starting from the head node
visited = [False] * (n+1)

def dfs(node):
    visited[node] = True
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs(neighbor)

dfs(head)

# Count the number of unreachable nodes
unreachable_nodes = 0
for i in range(1, n+1):
    if not visited[i]:
        unreachable_nodes += 1

print(unreachable_nodes)
