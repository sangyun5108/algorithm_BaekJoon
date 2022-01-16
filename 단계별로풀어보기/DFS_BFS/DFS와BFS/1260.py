from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph,i,visited)


n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    l,r = map(int,input().split())
    graph[l].append(r)
    graph[r].append(l)

[g.sort() for g in graph]


dfs(graph,v,visited)
print()
visited = [False for _ in range(n+1)]
bfs(graph,v,visited)