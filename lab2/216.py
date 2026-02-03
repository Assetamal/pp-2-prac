a = int(input())
num = list(map(int , input().split()))
seen = set()
for i in num:
    if i in seen:
        print("NO")
    else:
        print("YES")  
        seen.add(i)  