from collections import deque

n,m = map(int,input().split())

graph = [list(map(int,input())) for _ in range(m)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

