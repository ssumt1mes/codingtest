computer = int(input())
connected_computer = int(input())
connect_list = [[] for _ in range(100)]
visited = []
for i in range(connected_computer) :
    lists = (list(map(int,input().split())))
    connect_list[lists[0]].append(lists[1])
    connect_list[lists[1]].append(lists[0])
print(connect_list)