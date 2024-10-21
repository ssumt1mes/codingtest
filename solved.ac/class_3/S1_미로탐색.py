N,M = map(int,input().split())
list_maze = []
for i in range(N) :
    K = list(map(int,input()))
    list_maze.append(K)

x_index = 0
y_index = 0
count = 0
result = ''
empty_list = []

def search_index(list_maze,empty_list,x_index,y_index) :
    if(x_index!=0) : 
        if(list_maze[x_index-1][y_index]==1) :
            empty_list.append(x_index-1,y_index,)
    if(x_index!=N) :
        list_maze[x_index+1][y_index]
    if(y_index!=0) :
        list_maze[x_index][y_index-1]
    if(y_index!=M) :
        list_maze[x_index][y_index+1]
while(result!='Finish') :
    if(list_maze[x_index][y_index]==1) :
        
