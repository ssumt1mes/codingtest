from collections import deque
T = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]

#bfs로 풀었음
def find_bug(list,i,j,M,N) :
    queue = deque()
    queue.append((i,j))
    list[i][j] == 0
    while queue :
          x,y = queue.popleft()
          for i in range(4) :
                nx = x+dx[i]
                ny = y+dy[i]
                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                            continue
                if list[nx][ny] ==1 :
                      list[nx][ny] = 0
                      queue.append((nx,ny))
    return queue

for _ in range(T) :
    count = 0
    M,N,K = map(int,input().split())
    list = [[0]*N for _ in range(M)]
    for _ in range(K) :
        i,j = map(int,input().split())
        list[i][j] = 1
    
    for i in range(M) :
          for j in range(N) :
                if(list[i][j]==1) :
                      find_bug(list,i,j,M,N)
                      count+=1
    print(count)




        