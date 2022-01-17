n = int(input())
m = int(input())

# 그래프 정리

graph = [[] for _ in range(n+1)]

visited = [False for _ in range(n+1)]

result = 0

for i in range(m):
    l,r = list(map(int,input().split()))
    graph[l].append(r)
    graph[r].append(l)

[g.sort() for g in graph]

def dfs(graph,v,visited):
    global result
    visited[v] = True
    result += 1

    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(graph,i,visited)

dfs(graph,1,visited)

print(result-1)