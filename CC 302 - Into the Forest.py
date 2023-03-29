def dfs(node, visited, adj_list):
    visited[node] = True
    size = 1
    for neighbour in adj_list[node]:
        if not visited[neighbour]:
            size += dfs(neighbour, visited, adj_list)
    return size

n, m = map(int, input().split())

adj_list = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u-1].append(v-1)
    adj_list[v-1].append(u-1)

visited = [False] * n
tree_sizes = []
num_trees = 0

for i in range(n):
    if not visited[i]:
        size = dfs(i, visited, adj_list)
        num_trees += 1
        tree_sizes.append(size)

print(max(tree_sizes), min(tree_sizes), num_trees)
