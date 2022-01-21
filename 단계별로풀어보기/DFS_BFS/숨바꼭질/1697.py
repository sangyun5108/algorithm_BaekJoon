from collections import deque

n,k = map(int,input().split())

queue = deque()
queue.append(n)

MAX = 100000

graph = [0]*(MAX+1)

def bfs():
    while queue:
        x = queue.popleft()
        if x == k:
            break
        for i in (x+1,x-1,2*x):
            if 0<=i<=MAX and graph[i]==0:
                graph[i] = graph[x]+1
                queue.append(i)

bfs()

print(graph[k])

