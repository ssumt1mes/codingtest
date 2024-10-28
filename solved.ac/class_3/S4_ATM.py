N = int(input())
list_ATM = list(map(int,input().split()))
list_ATM.sort()
sum = 0
before = 0
for i in list_ATM :
    sum += i + before
    before += i
print(sum)