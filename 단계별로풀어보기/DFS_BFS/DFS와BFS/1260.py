from collections import deque

def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph,i,visited)
            

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


n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    r,l = map(int,input().split())
    graph[r].append(l)
    graph[l].append(r)

[g.sort() for g in graph]

dfs(graph,v,visited)
visited = [False for _ in range(n+1)]
print()
bfs(graph,v,visited)