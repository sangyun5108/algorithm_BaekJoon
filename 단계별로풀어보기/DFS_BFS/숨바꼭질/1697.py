from collections import deque

MAX = 100000

n,k = map(int,input().split())

graph = [0]*(MAX+1)

queue = deque()
queue.append(n)

def bfs():
    while queue:
        x = queue.popleft()
        if x == k:
            break
        
        for i in (x+1,x-1,2*x):
            if 0<=i<=MAX and graph[i]==0:
                queue.append(i)
                graph[i] = graph[x]+1


bfs()

print(graph[k])