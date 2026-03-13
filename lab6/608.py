a = int(input())
b = list(map(int , input().split()))
c = sorted(set(b))
for i in c:
    print(i , end=" ")