from collections import deque

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(graph,x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    count = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                count+=1
    return count

answer = []

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            answer.append(bfs(graph,i,j))

answer.sort()

print(len(answer))

for i in answer:
    print(i)