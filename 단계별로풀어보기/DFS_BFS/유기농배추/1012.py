test_case = int(input())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(graph,x,y):
    graph[x][y] = 0
    count = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        
        if graph[nx][ny] == 1:
            graph[nx][ny] == 0
            count+=1
            dfs(graph,nx,ny)
    return count

answer = []

for i in range(test_case):
    m,n,k = map(int,input().split())
    num = []

    graph = [[0]*n for _ in range(m)]

    for j in range(k):
        x,y = map(int,input().split())
        graph[x][y] = 1
    
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                num.append(dfs(graph,i,j))

    answer.append(len(num))
    num = []
    graph = [[0]*m for _ in range(n)]


for i in answer:
    print(i)
