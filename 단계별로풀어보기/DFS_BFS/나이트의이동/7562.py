from collections import deque

test_case = int(input())

dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,1,-1]

answer = []

def bfs():
    while queue:
        x,y = queue.popleft()
        if x == a and b == y:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))


for i in range(test_case):
    n = int(input())
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    graph = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append((x,y))
    bfs()
    answer.append(graph[a][b])


for i in answer:
    print(i)