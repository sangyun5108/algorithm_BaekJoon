from collections import deque

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(m)]

answer = 0

queue = deque()

dx = [-1,0,1,0]
dy = [0,1,0,-1]

res = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append(((i,j)))

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
                
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))


bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res,max(i))

print(res-1)